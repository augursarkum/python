import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Ensure you have the necessary nltk data downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Load your dataset (make sure the dataset is a CSV file with 'text' and 'sentiment' columns)
data = pd.read_csv('social_media_posts.csv')

# Data cleaning function
def clean_text(text):
    text = re.sub(r'@\w+', '', text)  # Remove @mentions
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    return text

# Apply data cleaning
data['clean_text'] = data['text'].apply(clean_text)

# Tokenization and stopword removal
stop_words = set(stopwords.words('english'))
data['tokenized_text'] = data['clean_text'].apply(lambda x: [word for word in word_tokenize(x) if word not in stop_words])

# Join tokens back into a string
data['processed_text'] = data['tokenized_text'].apply(lambda x: ' '.join(x))

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['processed_text'])

# Sentiment analysis (assuming binary sentiment: 'positive' and 'negative')
y = data['sentiment']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

