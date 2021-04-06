from math import sqrt
import numpy as np 
import pandas as pd 

class KNeighborsClassifier():
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors
    
    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, predict_X):
        all_distances = []
        for row_index, row in enumerate(self.X):
            total_distance = 0
            for value_index, value in enumerate(row):
                total_distance += sqrt((value - predict_X[0][value_index]) ** 2)
            all_distances.append((total_distance, self.y[row_index][0]))
        lowest_n_distances = sorted(all_distances)[:self.n_neighbors]
        labels = set(item[1] for item in lowest_n_distances)

        category_counts = {label: 0 for label in labels}

        for distance in lowest_n_distances:
            category_counts[distance[1]] += 1
        prediction = max(category_counts, key=category_counts.get)
        
        return prediction
