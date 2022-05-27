import re
import nltk
from datetime import datetime
from nltk.tokenize import RegexpTokenizer

import profanity

# pip install git+https://github.com/robsonpessoa/LeIA.git@0.1.2#egg=LeIA
from LeIA import leia


def find_verified(user_id: str, users: list) -> bool:
    default = {"verified": False}
    userfound = next((u for u in users if u["id"] == user_id), default)
    return userfound["verified"]


def analyze(textstr: str, verified: bool, date: str) -> dict:
    sentiment_analyzer = leia.SentimentIntensityAnalyzer()
    result = sentiment_analyzer.polarity_scores(textstr)
    positivity = result["compound"] > 0

    text_nolinks = re.sub(r'http\S+', '', textstr)
    regexp = RegexpTokenizer(r'\w+')
    onlytext = ' '.join(regexp.tokenize(text_nolinks))
    words = nltk.word_tokenize(onlytext)
    stopwords = nltk.corpus.stopwords.words("portuguese")
    frequency = nltk.FreqDist([word.lower() for word in words if
                               word.lower() not in stopwords and not word.lower().startswith(profanity.getlist())])

    # dateparsed = datetime.strptime(date[:-5], "%Y-%m-%dT%H:%M:%S")

    return {
        "sentiment": positivity,
        "frequent": frequency.most_common(10),
        "verified": verified,
        "date": date
    }
