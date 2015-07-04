# -*- coding:utf-8 -*-
__author__ = 'liuqianchao'
import logging
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
import sklearn.cross_validation
from sklearn.learning_curve import learning_curve,validation_curve

from sklearn import metrics
from pprint import pprint
def calculate_result(actual,pred):
    precision=metrics.precision_score(actual,pred)
    recall=metrics.recall_score(actual,pred)
    f1=2*(precision*recall)/(precision+recall)
    print 'precision:{0:.4f}'.format(precision)
    print 'recall:{0:0.4f}'.format(recall);
    print 'f1-score:{0:.4f}'.format(f1);
if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    warnings.filterwarnings("ignore")
    target={'Pos','Neg'}
    categories=['alt.atheism','comp.graphics','comp.os.ms-windows.misc','sci.electronics'];#'comp.sys.ibm.pc.hardware'
    newsgroup_train = fetch_20newsgroups(subset = 'train' ,categories=categories);
    newsgroups_test = fetch_20newsgroups(subset = 'test',categories=categories);
    tv = TfidfVectorizer(sublinear_tf = True,max_df = 0.5,stop_words = 'english');

    #训练集向量化
    sklearn.cross_validation.train_test_split(newsgroup_train.data, newsgroup_train.target, test_size=0.9, random_state=0)

    tfidf_train = tv.fit_transform(newsgroup_train.data)
    tv2 = TfidfVectorizer(vocabulary = tv.vocabulary_);
    tfidf_test = tv2.fit_transform(newsgroups_test.data);
    #print "the shape of train is "+repr(tfidf_train.shape)
    #print "the shape of test is "+repr(tfidf_test.shape)

    #nb
    from sklearn.naive_bayes import MultinomialNB
    from sklearn import metrics
    logging.info('NB')
    #create the Multinomial Naive Bayesian Classifier
    clf = MultinomialNB(alpha = 0.01)
    clf.fit(tfidf_train,newsgroup_train.target);
    pred = clf.predict(tfidf_test);
    calculate_result(newsgroups_test.target,pred);


    #knn
    from sklearn.neighbors import KNeighborsClassifier
    logging.info('k-NN')
    knnclf = KNeighborsClassifier()#default with k=5
    knnclf.fit(tfidf_train,newsgroup_train.target)
    pred = knnclf.predict(tfidf_test);
    calculate_result(newsgroups_test.target,pred);

    #svm
    from sklearn.svm import SVC
    logging.info('SVM')
    svclf = SVC(kernel = 'linear')#default with 'rbf'
    svclf.fit(tfidf_train,newsgroup_train.target)
    pred = svclf.predict(tfidf_test);
    calculate_result(newsgroups_test.target,pred);

