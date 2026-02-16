# O(t x N x K x d), where t is the number of iterations

import torch
import numpy as np

def k_means(data, K, max_iters = 100):
    # K: number of clusters
    N, d = data.shape
    centers = data[np.random.choice(N, K, replace=False)] # initialize centers by random K samples
    labels_prev = np.zeros(N, dtype=int)

    for _ in range(max_iters):
        tmp = data.reshape(N, 1, d) - centers.reshape(1, K, d) # (N, K, d)

        dists = np.sum(tmp ** 2, axis=-1) # (N, K)
        labels = np.argmin(dists, axis=-1) # (N,)

        for i in range(K):
            # recompute centers
            if np.any(labels == i):
                centers[i] = data[labels == i].mean(dim=0)
        
        if np.all(labels == labels_prev):
            # converged, stop early
            break
        
        labels_prev = labels.copy() # update previous labels, avoid reference issue
    
    return centers, labels