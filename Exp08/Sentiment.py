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

# Loop to take user input until they choose to stop
while True:
    user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the sentiment analysis program.")
        break
    
    sentiment = analyze_sentiment(user_input)
    print(f"Text: '{user_input}'\nSentiment: {sentiment}\n")
