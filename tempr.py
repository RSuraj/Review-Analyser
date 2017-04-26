import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import pickle
from sklearn.pipeline import Pipeline

def sentiment_analysis(input):

#if __name__ == '__main__':

    #if len(sys.argv) < 2:
     #   usage()
      #  sys.exit(1)

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
    temp=[]
    #est_review = input("enter the string.")
    temp.append(input)

    test_vectors = vectorizer.transform(temp).toarray()
    
    # Perform classification with SVM, kernel=rbf
    classifier_rbf =  svm.SVC(kernel='linear')
    classifier_rbf.fit(train_vectors, train_labels)
    classifier_rbf.predict(test_vectors)

    
   
    return prediction_rbf[0]

    # Perform classification with SVM, kernel=linear
    #classifier_linear = svm.SVC(kernel='linear')
    #t0 = time.time()
    #classifier_linear.fit(train_vectors, train_labels)
    #t1 = time.time()
    #prediction_linear = classifier_linear.predict(test_vectors)
    #t2 = time.time()
    #time_linear_train = t1-t0
    #time_linear_predict = t2-t1

    # Perform classification with SVM, kernel=linear
    #classifier_liblinear = svm.LinearSVC()
    #t0 = time.time()
    #classifier_liblinear.fit(train_vectors, train_labels)
    #t2 = time.time()
    #time_liblinear_train = t1-t0
    #time_liblinear_predict = t2-t1

    # Print results in a nice table
    #print("Results for SVC(kernel=rbf)")
    #print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    #rint(classification_report(test_labels, prediction_rbf))
    #print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    #print(classification_report(test_labels, prediction_linear))
    #print("Results for LinearSVC()")
    #print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    #print(classification_report(test_labels, prediction_liblinear))

