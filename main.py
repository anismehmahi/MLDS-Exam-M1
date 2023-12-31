#!/usr/bin/env python
# coding: utf-8




'''
Variables: 
---------

data : diabetes health indicators original dataset
X : features dataset
Y : target labels
pred : list of predicted labels 

'''




from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')




def classifier(mat, model):
    '''
    Predict using the trained model

    Input:
    -----
        mat : NxM matrix 
        model : the model choice 
    Output:
    ------
        pred : list of predicted labels
    '''
    if model=='SVM':
        model = pickle.load(open("models/svm.pkl", "rb"))
        pred = model.predict(mat)
        
    elif model=='RF':
        model = pickle.load(open("models/modele_random_forest.pkl", "rb"))
        pred = model.predict(mat)
        
    elif model=='GBC':
        model = pickle.load(open("models/modele_xgb.pkl", "rb"))
        pred = model.predict(mat)
        
    else:
        raise Exception("Please select one of the three methods : SVM, RF, GBC")
    
    return pred




# Import data
data = pd.read_csv('data/date_validation_diabetes_health_indicators.csv')
data['Diabetes_012'] = data['Diabetes_012'].astype(int)

X = data.drop(columns=['Diabetes_012','Unnamed: 0'], axis=1)

y = data['Diabetes_012']



# Predict labels using trained models
models = ['RF', 'GBC','SVM']
for model in models:

    # Make prediction
    pred = classifier(X, model)

    # Evaluate model results
    accuracy = accuracy_score(pred, y)
    f1_macro = f1_score(pred, y, average='macro', zero_division=True)
    f1_micro = f1_score(pred, y, average='micro', zero_division=True)

    # Print results
    print(f'Model: {model}\n-----\nAccuracy: {accuracy:.2f} \nF1_macro: {f1_macro:.2f} \nF1_micro: {f1_micro:.2f} \n')
