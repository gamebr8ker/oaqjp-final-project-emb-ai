from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("IBM SWE Final Project")

@app.route('/')
def getSite():
    return render_template('index.html')


@app.route("/emotionDetector", methods=["GET"])
def emo_detector():
    
    ### Query the emotion_detector API
    nlp_text = request.args["textToAnalyze"]
    emotion_dict = emotion_detector(nlp_text)


    ### Build the text response
    output_str1 = "For the given statement, the system response is "
    output_str3 = f" The dominant emotion is {emotion_dict['dominant_emotion']}."

    # Convert dict of {emotion : score} into an output string
    emotion_sub = emotion_dict.copy()
    emotion_sub.pop("dominant_emotion")
    
    output_str2 = ""
    for k,v in emotion_sub.items():
        output_str2 += ( ("\'" + k + "\'" + ": " + str(v) + ", ") )

    output_str2 = output_str2[:-2]    # remove trailing ", "

    # Combine all output strings into desired response
    response_text = output_str1 + output_str2 + output_str3


    return response_text


if __name__ == "__main__":
    app.run(debug=True)