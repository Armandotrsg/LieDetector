import pickle
from speech_recognition import recognize_from_microphone
from speech_recognition import from_file_continuous
from SentimentAnalysis import sentiment_analysis_with_opinion_mining
from SeperateAudioAndVideo import seperate_audio_and_video

def buildAI():
    """ vectorizer = CountVectorizer(lowercase = False, ngram_range = (1,3))
    df = pd.read_csv("MachineLearning/df.csv")
    xtrain, xtest, ytrain, ytest = train_test_split(df.light_normalization, df[["veracity"]], test_size = 0.3, random_state = 42)
    xtrain = vectorizer.fit_transform(xtrain)
    xtest = vectorizer.transform(xtest)
    ai = LogisticRegression().fit(xtrain, ytrain)
    print("Accuracy: ", ai.score(xtest, ytest)) """
    model = pickle.load(open("MachineLearning/model.pkl", "rb"))
    return model

def predict_statement(statement,model):
    #load the vectorizer
    vectorizer = pickle.load(open("MachineLearning/vectorizer.pkl", "rb"))
    statement = [statement]
    statement = vectorizer.transform(statement)
    prediction = model.predict(statement)
    if prediction == True:
        print("\nThe statement is true\n")
    else:
        print("\nThe statement is false\n")
    return prediction

def statement(file=None):
    model = buildAI()
    # Get the text
    if file is None:
        text = str(recognize_from_microphone())
    else:
        seperate_audio_and_video(file)
        text = from_file_continuous("audio.wav")
        #lowercase the text
        text = text.lower()
        text = text.replace("'", "")
        #add "" to the end of the text and the beginning
        text = '"' + text + '"'
  
    #Predict
    prediction = predict_statement(text,model)
    #Sentiment Analysis
    sentiment = sentiment_analysis_with_opinion_mining(text)
    return prediction, sentiment, text

    

