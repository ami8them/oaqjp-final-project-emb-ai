import requests
import json

#function with input variable "text_to_analyze"
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send POST request to API
    response = requests.post(url, json = myobj, headers=header)
    
    # Successful response
    if response.status_code == 200:
        # convert the response (string) to python dictionary
        formatted_response = json.loads(response.text)
        # extract the emotions as dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # analyze the scores and determine the dominant emotion
        dom_em = max(emotions, key=emotions.get) 
        # add the dominant emotion to dict
        emotions['dominant_emotion'] = dom_em
    # Invalid response, server errors ...
    else:
        emotions = {'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None}
    return emotions
