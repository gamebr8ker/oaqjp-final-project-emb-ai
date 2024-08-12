import requests
import json


# Placeholder
#text_to_analyze = "I love this new technology."
#text_to_analyze = "I am so happy I am doing this."


def emotion_detector(text_to_analyze):
    """
        Access Watson NLP Emotion Predict, via given URL, Headers, and JSON
        Assume text_to_analyze is a variable containing text to analyze

        Returns the text attribute of the response object
    """
    
    watson_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyze } }

    req = requests.post(url=watson_url, headers=headers, json=input_data)

    # Convert the request response to JSON
    req_json = json.loads(req.text)
    
    # Parse 'emotion' dict from the request response
    req_emotions = req_json['emotionPredictions'][0]['emotion']


    # Find the dominant Emotion and Score (highest-scoring emotion from dict)
    highest_score = 0
    dominant_emote = ""
    for key in req_emotions:
        if req_emotions[key] > highest_score:
            dominant_emote = key
            highest_score = req_emotions[key]

    # Add 'dominant_emotion' to emotion dict
    req_emotions['dominant_emotion'] = dominant_emote

    return req_emotions


#test1 = emotion_detector(text_to_analyze)
#print(test1)