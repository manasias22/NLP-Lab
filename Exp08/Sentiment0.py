from textblob import TextBlob
 
def analyze_sentiment(text):
	# Create a TextBlob object
	blob = TextBlob(text)
	
	# Get the sentiment polarity
	polarity = blob.sentiment.polarity
	
	# Determine sentiment category
	if polarity > 0:
    	return "Positive"
	elif polarity < 0:
    	return "Negative"
	else:
    	return "Neutral"
 
# Sample texts for analysis
sample_texts = [
	"I love this product! It's amazing.",
	"This is the worst service I've ever experienced.",
	"The weather is okay today."
]
 
# Analyzing sentiment of sample texts
for text in sample_texts:
	sentiment = analyze_sentiment(text)
	print(f"Text: '{text}'\nSentiment: {sentiment}\n")
