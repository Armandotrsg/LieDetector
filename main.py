import cv2
import numpy as np
from eye_tracker import get_eye_pos
from head_pose_estimation import get_head_pose
from deceptionStatement import statement
from SentimentAnalysis import get_analysis
from face_detector import get_face_detector
from face_landmarks import get_landmark_model

#video
videoAnalyze = "clinton.mov"

#Text analysis
prediction, sentiment, text = statement(videoAnalyze)

#Eye tracker
face_model = get_face_detector()
landmark_model = get_landmark_model()
left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

cap = cv2.VideoCapture(videoAnalyze)
ret, img = cap.read()
thresh = img.copy()

cv2.namedWindow('image')
kernel = np.ones((9, 9), np.uint8)

#Head Pose Estimation

#cap = cv2.VideoCapture(0)
#ret, img = cap.read()
size = img.shape
font = cv2.FONT_HERSHEY_SIMPLEX 
# 3D model points.
model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-225.0, 170.0, -135.0),     # Left eye left corner
                            (225.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner
                        ])

# Camera internals
focal_length = size[1]
center = (size[1]/2, size[0]/2)
camera_matrix = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )

def nothing(x):
    pass
cv2.createTrackbar('threshold', 'image', 75, 255, nothing)

#Variables for head pose estimation
eyesLeft = 0
eyesRight = 0

headDown = 0
headLeft = 0
headRight = 0

while cap.isOpened():
    ret, img = cap.read()
    get_eye_pos(face_model,landmark_model,left,right,ret,img,thresh,kernel,eyesLeft,eyesRight)
    get_head_pose(face_model,landmark_model,ret,img,size,font,model_points,focal_length,center,camera_matrix,headDown,headLeft,headRight)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()        

positive = 0
negative = 0
neutral = 0

get_analysis(sentiment)
print("The statement is:\n", text)

for document in sentiment:
    if document.sentiment == "positive":
        positive += 1
    elif document.sentiment == "negative":
        negative += 1
    else:
        neutral += 1


if prediction: #If the prediction is true, we must check the sentiment
    print("The statement is true")
    #Analyze eyes and head pose
    if eyesLeft > 10 or eyesRight > 10 or headDown > 10 or headLeft > 10 or headRight > 10:
        print("The person is lying")
    else:
        if positive > negative:
            print("The person is telling the truth")
        else:
            print("The person is lying")
else: #If the prediction is false, then the person is lying
    print("The statement is false")
    print("The person is lying")





