# QAM Symbol Detection Based on Decision Tree
# 16 QAM modulation generates 16 different complex signals
# Signal transmission is subject to noise pollution, producing error: Srx = Stx + n, n is complex Gaussian noise
# Stx = -1 + 1j
# n = 0.38 - 1.2j
# Srx = (-1 + 0.38) + (1 - 1.2)j = -0.62 - 0.2j

# Wireless signal decision outputs its true transmitted symbol based on received QAM symbol

# Use CART decision tree to implement a simple QAM symbol classifier

# Build decision tree based on M received symbols and true labels
# Splitting criterion is Gini coefficient
# Decision tree max depth 5
# Feature value split point limit: {-3, -2, -1, 0, 1, 2, 3}

# Output Gini coefficient of training set, keep 4 decimal places
# Output verification QAM symbol label

# Input
from collections import Counter


M = int(input()) # Sample count 10 ~ 20
# Each sample contains two features: real and imaginary parts, and true label (0 ~ 15)
data = [list(map(float, input().split())) for _ in range(M)]
X = [ [sample[0], sample[1]] for sample in data ] # Features
y = [ int(sample[2]) for sample in data ]         # Labels    
# One verification sample
test_sample = list(map(float, input().split()))

# Calculate Gini index of sample set
def gini_index(labels):
    total = len(labels)
    if total == 0:
        return 0.0
    cnt = Counter(labels)
    p = [count / total for count in cnt.values()]
    gini = 1 - sum(pi ** 2 for pi in p)
    return gini

# Find label
def label(idxs, y):
    labels = [y[i] for i in idxs]
    cnt = Counter(labels)
    max_count = max(cnt.values())
    return min(label for label, count in cnt.items() if count == max_count)

# Tree node definition
class TreeNode:
    def __init__(self):
        self.is_leaf = True
        self.label = 0
        self.feature_index = -1
        self.threshold = 0.0
        self.left = None
        self.right = None


# Build decision tree
THRESHOLDS = [-3, -2, -1, 0, 1, 2, 3]

def build_tree(X, y, idxs, depth_limit):
    node = TreeNode()
    current_labels = [y[i] for i in idxs]
    curr_gini = gini_index(current_labels)

    if curr_gini == 0 or depth_limit == 0:
        node.is_leaf = True
        node.label = label(idxs, y)
        return node
    
    best_gini = float('inf')
    best_feature = -1
    best_threshold = 0.0
    best_left, best_right = None, None

    # Iterate over all features and split points
    for feature_index in [0, 1]:
        for t in THRESHOLDS: # Directly use t as split point
            left_idxs = [i for i in idxs if X[i][feature_index] < t]
            right_idxs = [i for i in idxs if X[i][feature_index] >= t]

            if not left_idxs or not right_idxs: # One side is empty, unreasonable split
                continue

            left_labels = [y[i] for i in left_idxs]
            right_labels = [y[i] for i in right_idxs]

            gini_left = gini_index(left_labels)
            gini_right = gini_index(right_labels)

            weighted_gini = (len(left_idxs) * gini_left + len(right_idxs) * gini_right) / len(idxs)

            # Update condition
            # 1. gini is smaller
            # 2. when gini is equal, choose smaller feature index
            # 3. when feature index is also equal, choose smaller split point
            if weighted_gini < best_gini - 1e-12 or (abs(weighted_gini - best_gini) <= 1e-12 and (feature_index < best_feature or (feature_index == best_feature and t < (best_threshold if best_threshold is not None else 0)))):
                best_gini = weighted_gini
                best_feature = feature_index
                best_threshold = t
                best_left = left_idxs   
                best_right = right_idxs
    
    if best_left is None or best_gini >= curr_gini - 1e-12: # Cannot split or split is worse
        node.is_leaf = True
        node.label = label(idxs, y)
        return node
    # Continue splitting
    node.is_leaf = False
    node.feature_index = best_feature
    node.threshold = best_threshold
    node.left = build_tree(X, y, best_left, depth_limit - 1)
    node.right = build_tree(X, y, best_right, depth_limit - 1)
    return node

# Gini coefficient of the entire sample set, calculated directly
train_labels = [y[i] for i in range(M)]
train_gini = gini_index(train_labels)
print(f"{train_gini:.4f}")

root = build_tree(X, y, list(range(M)), 5)

# Prediction function
def predict(sample, node):
    if node.is_leaf:
        return node.label
    if sample[node.feature_index] < node.threshold:
        return predict(sample, node.left)
    else:
        return predict(sample, node.right)

predicted_label = predict(test_sample, root)
print(predicted_label)