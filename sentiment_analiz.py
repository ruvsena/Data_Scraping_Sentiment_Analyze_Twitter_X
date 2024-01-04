

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment =SentimentIntensityAnalyzer()
d = open("tweetler_en.txt","r", encoding="utf-8")
sent=sentiment.polarity_scores(d)
print(sent)









