# importing kivy moduels
from kivy.app import App
import kivy
kivy.require('1.11.1')
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
# ending importing kivy moduels
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

class Application(App):
    def build(self):
        # creating our layout. we want it to display objects vertically
        self.layout = BoxLayout(orientation='vertical')
        # creating the submit review button, our review field, the label displaying the prediction and the correct and incorrect buttons that are useful to re-train the model
        submit_button = Button(text='classify feedback', on_press=self.classify_f)
        self.review = TextInput(hint_text='Your laptop popularity detection')
        self.label = Label()  
        self.layout.add_widget(self.review)
        self.layout.add_widget(submit_button)
        self.layout.add_widget(self.label)
        return self.layout

    def classify_f(self, action):
        print(self.review.text)
        pred, proba = classify(self.review.text)
        print(pred)
        print(str(round(proba, 2)*100) + " % ")
        self.label.text = pred + "  " + str(round(proba, 2)*100) + " % "


if __name__ == '__main__':
    # running the application
    Application().run()