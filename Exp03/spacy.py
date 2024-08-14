import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "There is a pen on the table"

# Process the text using spaCy
doc = nlp(text)

# Remove stopwords
filtered_words = [token.text for token in doc if not token.is_stop]

# Join the filtered words to form a clean text
clean_text = ' '.join(filtered_words)

print("Original Text:", text)
print("Text after Stopword Removal:", clean_text)
