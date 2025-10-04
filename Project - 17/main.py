from sklearn.base import TransformerMixin,BaseEstimator
from collections import Counter
from nltk import PorterStemmer
from joblib import load
import numpy as np
import streamlit as st
stemmer = PorterStemmer()
class Vectorizer(TransformerMixin,BaseEstimator):
    def __init__(self,vocab_size=50):
        self.vocab_size = vocab_size
    def fit(self,X,y=None):
        self.letters = []
        self.textARR = []
        for i in X:
            self.letters.append([stemmer.stem(word) for word in i.split()])
        for i in self.letters:
            for text in (" ".join(i)).split():
                self.textARR.append(text)
        
        self.textCounter = Counter(self.textARR)
        self.vocab_ = [a[0] for a in self.textCounter.most_common()[:self.vocab_size]]
        return self
    def transform(self,X,y=None):
        Vectors=[]
        for letter in X:
            letter = [stemmer.stem(word) for word in letter.split()]
            MinVector =[]
            for VocWord in self.vocab_:
                if VocWord in letter:
                    MinVector.append(1)
                else: 
                    MinVector.append(0)
            Vectors.append(MinVector)
       ## print(Vectors)
        return np.array(Vectors)
vectorizer = load("vectorizer.joblib")
model = load("model.joblib")
st.header("Love Letter Detection")
with st.container():
    data = st.text_input("Enter your Letter")
    if st.button("Classify",key="1"):
        st.success("Its a love😍 letter!" if model.predict(vectorizer.transform([data]))[0]==1 else "Its not a love😥 letter.")
        st.balloons()