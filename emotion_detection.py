import requests

#function with input variable "text_to_analyze"
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send POST request to API
    response = requests.post(url, json = myobj, headers=header)
    # return response as text
    return response.text
