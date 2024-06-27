from flask import Flask, request
from src.Model import SentimentModel
from user_html import Result

USER=Result()

app = Flask(__name__)
sentiment_model = SentimentModel()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = sentiment_model.predict_sentiment(text)
    return USER.generate_html(sentiment)


if __name__ == '__main__':
    app.run(debug=True)





