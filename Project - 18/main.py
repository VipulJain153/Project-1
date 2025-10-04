import streamlit as st
from collections import Counter
from nltk import PorterStemmer
from scipy.sparse import csr_matrix
import re
from sklearn.base import TransformerMixin,BaseEstimator
from joblib import load
stemmer = PorterStemmer()
class Vectorizer(BaseEstimator,TransformerMixin):
    def __init__(self,vocab_size=10):
        self.vocab_size = vocab_size
    def fit(self,X,y=None):
        PrevGodCounter = Counter()
        GodCounter = Counter()
        counters = self.process(X)
        for counter in counters:
            for word,count in counter.items():
                PrevGodCounter[word]+=count
        for word,count in PrevGodCounter.most_common()[:self.vocab_size]:
            GodCounter[word] = count
        self.vocab = {word:i+1 for i,(word,count) in enumerate(GodCounter.most_common()[:self.vocab_size])}
        return self
    def transform(self,X,y=None):
        counters = self.process(X)
        rows=[]
        cols=[]
        data=[]
        for row,counter in enumerate(counters):
            for word,count in counter.items():
                rows.append(row)
                cols.append(self.vocab.get(word,0))
                data.append(count)
        return csr_matrix((data,(rows,cols)),shape=(len(counters),self.vocab_size+1))
    def process(self,X):
        counters = []
        texts = []
        for i in X:
            texts.append(stemmer.stem(re.sub(r"[^\w\s]","",i)))
        for i in texts:
            counters.append(Counter(i.split()))
        return counters
model = load("model.joblib")
vectorizer = load("vectorizer.joblib")
st.header("Sentiment Rating Detection")
txt = st.text_input("Enter the text...")
if st.button("Check"):
    ans = model.predict(vectorizer.transform([txt]))[0]
    match ans:
        case 0:
            st.success("Excellent Rating")
            st.balloons()
        case 1:
            st.success("Good Rating")
            st.balloons()
        case 2:
            st.success("Neutral Rating")
            st.balloons()
        case 3:
            st.success("Bad Rating")
            st.balloons()
        case 4:
            st.success("Worse Rating")
            st.balloons()