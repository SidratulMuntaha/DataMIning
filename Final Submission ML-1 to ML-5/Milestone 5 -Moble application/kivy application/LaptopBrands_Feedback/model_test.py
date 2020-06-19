# model_test.py

import pickle
import os
import numpy as np
from vectorizer import vect


current_dir = os.path.dirname(__file__)
# we load the classifier.pkl we created before
clf = pickle.load(open(os.path.join(current_dir,
                 'pkl_objects',
                 '/Users/sidratulmuntaha/PycharmProjects/LaptopBrands_Feedback/classifier.pkl'), 'rb'))


def classify(document):
	# this dictionary returns as outputs 'negative ' or 'positive' instead of 0 or 1
    label = {0: 'negative', 1: 'positive'}
    # transforming the document into analyzable data
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba


if __name__ == '__main__':
    prediction, probability = classify("Mac is ok to work with")
    print("Prediction : " + prediction)
    print("Probability : " + str(round(probability * 100, 1)) + ' %')