from flask import Flask, render_template
from speech_to_text import speech_to_text
from preprocessing import preprocess
from sentiment import get_sentiment
from confidence import confidence_score
from final_score import final_interview_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    text = speech_to_text()
    words = preprocess(text)

    sentiment, polarity = get_sentiment(text)
    confidence = confidence_score(words)
    final_score = final_interview_score(confidence, polarity)

    return render_template(
        "result.html",
        answer=text,
        sentiment=sentiment,
        confidence=confidence,
        final_score=final_score
    )

if __name__ == "__main__":
    app.run(debug=True)
