#seperate audio and video from a file
import moviepy.editor

#seperate_audio_and_video("test.mp4")
def seperate_audio_and_video(file):
    clip = moviepy.editor.VideoFileClip(file)
    clip.audio.write_audiofile("audio.wav")
    #clip.write_videofile("video.mp4")
    clip.close()
        




