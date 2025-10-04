from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from collections import Counter
from nltk import PorterStemmer
from scipy.sparse import csr_matrix
import re
from sklearn.base import TransformerMixin,BaseEstimator
from joblib import load
stemmer = PorterStemmer()
import os
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
app = Flask(__name__)
app.app_context().push()
db_path = os.path.join(os.path.dirname(__file__), 'todo.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class Ratings(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    result = db.Column(db.String(500))
    def __repr__(self)->str:
        return self.result
result = None
@app.route("/",methods=["GET", "POST"])
def index():
    if request.method=="POST":
        rating =request.form["rating"]
        ans = model.predict(vectorizer.transform([rating]))[0]
        match ans:
            case 0:
                ans = 5
            case 1:
                ans = 4
            case 2:
                ans = 3
            case 3:
                ans = 2
            case 4:
                ans = 1
        a=Ratings(result=f"{ans} Star")
        db.session.add(a)
        db.session.commit()
        return render_template("index.html",result=f"{ans} Star")
    return render_template("index.html",result=result)
@app.route("/about")
def about():
    return render_template("about.html",result=Ratings.query.all())
if __name__ == "__main__":
    app.run(debug=True)