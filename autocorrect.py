#Enter the string,and it wll be changed by autocorrect if required
from textblob import TextBlob
text = raw_input("Enter the string:")
print "After AutoCorrect:",TextBlob(text).correct()
