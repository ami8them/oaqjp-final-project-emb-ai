''' Executing this function initiates the emotion detection APP
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detect():
    ''' This code receives the text from the HTML interface and 
        runs an emotion detection. The output returned is a dictionary
        with emotions and their scores plus name the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # run the text through emotion_detector and store the output dict
    response = emotion_detector(text_to_analyze)
    # Return it as a formatted text
    return (f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is <b>{response['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    ''' render HTML template
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' deploys flask app on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000) 
