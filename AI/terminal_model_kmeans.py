# Terminal Model Clustering Recognition
# Recognize terminal model based on terminal features

# Four features: packet interval duration, connection duration, signal strength before roaming, signal strength after roaming
# k types of terminals
# Use k-means clustering algorithm for recognition

# No class of terminal has 0 instances
# Input data is already normalized

# Initial k centroids are the first k sample points

def distance(a, b):
    """Calculate Euclidean distance between two sample points"""
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

# Termination condition: centroids no longer change or max iterations reached

k, m, n = map(int, input().split())

data = [list(map(float, input().split())) for _ in range(m)]

# Initialize centroids
centroids = data[:k]
MAX_ITER = n

iter_count = 0
while iter_count < MAX_ITER:
    clusters = [[] for _ in range(k)]
    
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    
    new_centroids = []
    for cluster in clusters:
        new_centroid = [sum(features) / len(cluster) for features in zip(*cluster)]
        new_centroids.append(new_centroid)
    
    if new_centroids == centroids:
        break

    centroids = new_centroids
    iter_count += 1

# Sort by terminal quantity from small to large
counts = [len(cluster) for cluster in clusters]
counts.sort()
print(' '.join(map(str, counts)))