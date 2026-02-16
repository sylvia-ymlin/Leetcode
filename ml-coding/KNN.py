# KNN is a simple, instance-based learning algorithm used for classification and regression tasks. It predicts the label of a data point based on the labels of its k nearest neighbors in the feature space.

import numpy as np


def knn_predict(X_train, y_train, x_query, k):
    distances = np.linalg.norm(X_train - x_query, axis=1)
    # get the nearest neighbor indices
    neighbor_indices = np.argsort(distances)[:k]
    # get the labels of the nearest neighbors
    neighbor_labels = y_train[neighbor_indices]

    # majority vote for classification
    values, counts = np.unique(neighbor_labels, return_counts=True) # get unique labels and their counts
    majority_label = values[np.argmax(counts)] # label with the highest count

    return majority_label
