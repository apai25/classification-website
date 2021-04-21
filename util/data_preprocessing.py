import numpy as np 
import pandas as pd 

def preprocess_data():
    training_data = pd.read_csv('flaskr/data/training_data.csv', header=None) 
    prediction_data = pd.read_csv('flaskr/data/prediction_data.csv', header=None)

    X_train = training_data.iloc[:, :-1].values 
    y_train = training_data.iloc[:, -1:].values

    test = np.array(prediction_data)
    return X_train, y_train, test
