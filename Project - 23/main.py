import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Load the data
data = pd.read_csv("IMDB Dataset.csv")

# Split the data
train_set, test_set = train_test_split(data, random_state=42, test_size=0.2)

# Define a preprocessor function
def preprocess_text(text):
    # Include your pre-processing steps here (HTML tag removal, noise removal, stemming, etc.)
    # For simplicity, let's just perform lowercasing here
    return text.lower()

# Apply preprocessor to the text column
train_set['review'] = train_set['review'].apply(preprocess_text)
test_set['review'] = test_set['review'].apply(preprocess_text)

# Vectorize the data using CountVectorizer
vectorizer = CountVectorizer(max_features=1000)  # Adjust max_features as needed
train_set_transformed = vectorizer.fit_transform(train_set['review'])
test_set_transformed = vectorizer.transform(test_set['review'])
print(train_set_transformed.toarray()[0])
# Define and train AdaBoostClassifier with RandomForestClassifier as base estimator
# model = AdaBoostClassifier(base_estimator=RandomForestClassifier(n_estimators=50),
#                            n_estimators=50, learning_rate=0.5, random_state=42)

# model.fit(train_set_transformed, train_set['sentiment'])

# # Predictions on the training set
# train_predictions = model.predict(train_set_transformed)
# train_confusion_matrix = confusion_matrix(train_set['sentiment'], train_predictions)

# # Predictions on the test set
# test_predictions = model.predict(test_set_transformed)
# test_confusion_matrix = confusion_matrix(test_set['sentiment'], test_predictions)

# print("Confusion Matrix (Training Set):")
# print(train_confusion_matrix)

# print("\nConfusion Matrix (Test Set):")
# print(test_confusion_matrix)
