import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import MultinomialNB 

def predict(sample):
    data = pd.read_csv('data/spam.csv',encoding='Windows-1252')

#     print(data.head())
    x = np.array(data["message"])
    y = np.array(data["class"])
    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train,y_train)

#    sample = input('Enter a message:')
    data = cv.transform([sample]).toarray()
    return (clf.predict(data))

#predict('hello world')