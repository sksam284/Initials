from textblob import TextBlob
text = raw_input("Enter the tweet:")
print "nearer to 1 means a positive sentiment and values nearer to -1 means a negative sentiment"
sentiment = TextBlob(text).sentiment[0]
if sentiment==0:
    mode = "neutral"
elif sentiment<0:
    mode = "sad"
elif sentiment>0:
    mode = "happy"
print "sentiment of tweet is:%s , with order: %s"%(mode, sentiment)
