from textblob import TextBlob
text = raw_input("Enter the tweet:")
print "nearer to 1 means a positive sentiment and values nearer to -1 means a negative sentiment"
print "sentiment of tweet is:",TextBlob(text).sentiment[0]
