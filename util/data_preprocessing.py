import numpy as np # Importing the Numpy library. This library provides us with the class "ndarray", which is essentially a two-dimensional list that comes with in-built methods.
import pandas as pd # Importing the Pandas library. This library will provide functions that allow us to read data from a CSV file stream.

def preprocess_data():
    # pd.read_csv() is a Pandas function that reads data from a csv file (read from the inputted file path) and places it into a Pandas DataFrame, a special type of data structure.
    training_data = pd.read_csv('flaskr/data/training_data.csv', header=None) # Header=None simply signifies that there is no headings row in the data.
    prediction_data = pd.read_csv('flaskr/data/prediction_data.csv', header=None)

    # Iloc helps us index the Pandas DataFrame similarly to how we would a two-dimensional list. 
    X_train = training_data.iloc[:, :-1].values # .values is another Pandas DataFrame method. This converts the selected columns (selected using iloc) into a Numpy array. 
    y_train = training_data.iloc[:, -1:].values

    test = np.array(prediction_data) # np.array() simply converts a Pandas DataFrame to a Numpy array, which works just like a two-dimensional list.
    return X_train, y_train, test

