from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from twitter_trends import get_twitter_trends
from twitter_search import twitter_search
from tr import sentiment_analysis
from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from database import Base,Webdata
from sklearn.metrics import accuracy_score
import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import pickle
from sklearn.pipeline import Pipeline

app=Flask(__name__)
@app.route('/')
def starter():
  return render_template('landingpage.html')
@app.route('/home')
def frontpage():
  return render_template('index2.html')
@app.route('/', methods=['GET', 'POST'])
def userinput():
    if request.method=='POST':
        engine =create_engine('sqlite:///info.db')
        Base.metadata.bind = engine
        DBsession =sessionmaker (bind=engine)
        session=DBsession()
        
       
        da=request.form['submiter']
        data =request.form['review'] 
        dataB=Webdata(review=data)
        session.add(dataB)
        session.commit() 
        
        return render_template('index2.html')
    #else:html
@app.route('/results')
def results():
    data_dir = 'txt_sentoken'
    classes = ['pos', 'neg']

    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                train_data.append(content)
                train_labels.append(curr_class)
    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)

    
    # Perform classification with SVM, kernel=rbf
    classifier_rbf =  svm.SVC(kernel='linear')
    classifier_rbf.fit(train_vectors, train_labels)
    transfer=[]
    engine =create_engine('sqlite:///info.db')
    Base.metadata.bind = engine
    DBsession =sessionmaker (bind=engine)
    session=DBsession()
    fetchdata=session.query(Webdata).order_by("id desc")
    count=0
    pos=0
    neg=0
    for i in fetchdata:
            query=i.review
            temp=[]
            temp.append(query)
            test_vectors = vectorizer.transform(temp).toarray()
            prediction_rbf = classifier_rbf.predict(test_vectors)
    

    
    
            carry=prediction_rbf[0]
            if(carry=="pos"):
                pos=pos+1
            if(carry=="neg"):
                neg=neg+1    
            transfer.append({'query': query, 'carry' : carry})
            count=count+1
        
    flash("new menu item created")
    return render_template('Results.html',transfer=transfer,count=count,pos=pos,neg=neg)
        

if __name__=='__main__':
    app.secret_key='super_secret_key'
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
