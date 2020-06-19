import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")
import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

stop = set(stopwords.words('english'))

df = pd.read_csv('/Users/sidratulmuntaha/Sentiment_data.csv', encoding='utf-8')


def tokenizer(text):

  features = df.iloc[:, 1].values
  labels = df.iloc[:, 2].values

processed_features = []

for sentence in range(0, len(features)):
    # Remove all the special characters
    processed_feature = re.sub(r'\W', ' ', str(features[sentence]))

    # Remove numbers
    processed_feature = re.sub(r'[0-9]+', ' ', processed_feature)

    # Remove all single characters
    processed_feature = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

    # Remove single characters from the start
    processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature)

    # Substituting multiple spaces with single space
    processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

    # Removing prefixed 'b'
    processed_feature = re.sub(r'^b\s+', '', processed_feature)

    # Converting to Lowercase
    processed_feature = processed_feature.lower()

    processed_features.append(processed_feature)

    processed_features = pd.DataFrame(processed_features)
    processed_features.columns = ['TEXT']

    # tokenizing
    tokenized = processed_features['TEXT'].apply(lambda x: x.split())
    print(tokenized.head())

# creating the .pkl files

vect = HashingVectorizer(decode_error='ignore',
                         n_features=1000,
                         preprocessor=None,
                         tokenizer=tokenizer)

clf = SGDClassifier(loss='log', random_state=40, max_iter=2000, early_stopping=False)

# df = pd.read_csv('/Users/sidratulmuntaha/Sentiment_data.csv', encoding='utf-8')

X_train = df['TEXT'].values
y_train = df['SENTIMENTS'].values

X_train = vect.transform(X_train)
clf.fit(X_train, y_train)
# We fit the model with the reviews and labels of the dataset

pickle.dump(stop,
            open('stopwords.pkl', 'wb'),
            protocol=4)

pickle.dump(clf,
            open('classifier.pkl', 'wb'),
            protocol=4)
# creating the .pkl files
