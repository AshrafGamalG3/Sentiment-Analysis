
import joblib

MODEL = joblib.load('Model/sentiment_model.joblib')
VECTORIZER = joblib.load('Model/tfidf_vectorizer.joblib')




from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


class Preprocessing:

    def __init__(self):
        pass

    @staticmethod
    def clean_mentions(text: str):
        return re.sub(r"@[a-zA-Z0-9_]+", "", text)

    @staticmethod
    def clean_URLs(text: str):
        return re.sub(r"http\S+|www\S+|https\S+", "", text)

    @staticmethod
    def clean_HTML5_entities(text: str):
        return re.sub(r"&[a-z]+;", "", text)

    @staticmethod
    def clean_punctuations(text: str):
        return re.sub(r"\W", " ", text)

    @staticmethod
    def clean_numbers(text: str):
        return re.sub(r"[0-9]+", "", text)

    @staticmethod
    def clean_stopwords(text: str):
        return " ".join([token for token in text.split() if token not in STOP_WORDS])

    @staticmethod
    def lemmatize_text(text: str):
        return " ".join([LEMMATIZER.lemmatize(token, pos="v") for token in text.split()])

    @staticmethod
    def normalize(text: str):
        text = text.lower()
        text = Preprocessing.clean_mentions(text)
        text = Preprocessing.clean_URLs(text)
        text = Preprocessing.clean_HTML5_entities(text)
        text = Preprocessing.clean_punctuations(text)
        text = Preprocessing.clean_numbers(text)
        text = Preprocessing.clean_stopwords(text)
        text = Preprocessing.lemmatize_text(text)
        return text





class SentimentModel:

    def __init__(self):
        pass

    def preprocess_input(self, text):
        cleaned_text = Preprocessing.normalize(text)
        transformed_text = VECTORIZER.transform([cleaned_text]).toarray()
        return transformed_text

    def predict_sentiment(self, text):
        transformed_text = self.preprocess_input(text)
        prediction = MODEL.predict(transformed_text)
        sentiment_mapping = {0: 'Negative', 2: 'Neutral', 4: 'Positive'}
        sentiment = sentiment_mapping[prediction[0]]
        return sentiment

c=SentimentModel()
print(c.predict_sentiment("I am happy"))