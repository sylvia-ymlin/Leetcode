# 基于决策树的QAM调制符合检测
# 16 QAM 调制会生成 16 个不同的复数信号
# 信号传输过程中会受到噪声污染，产生误差： Srx = Stx + n, n 为复数高斯噪声
# Stx = -1 + 1j
# n = 0.38 - 1.2j
# Srx = (-1 + 0.38) + (1 - 1.2)j = -0.62 - 0.2j

# 无线信号根据接收到的 QAM 符号，判决输出其真实发送的符号

# 利用 CART 决策树，实现一个 简单的 QAM 符号分类器

# 根据输入的 M 个接收符号，和真实标签构建决策树
# 划分标准为 Gini 系数
# 决策树最大深度 5
# 特征值切分点限制：{-3, -2, -1, 0, 1, 2, 3} 

# 输出训练集的 Gini 系数，保留四位小数
# 输出验证 QAM 的符号标签

# 输入
from collections import Counter


M = int(input()) # 样本个数 10 ~ 20
# 每个样本包含两个特征：实部和虚部，和真实标签（0 ～ 15）
data = [list(map(float, input().split())) for _ in range(M)]
X = [ [sample[0], sample[1]] for sample in data ] # 特征
y = [ int(sample[2]) for sample in data ]         # 标签    
# 验证集一个样本
test_sample = list(map(float, input().split()))

# 计算样本集的 gini 指数
def gini_index(labels):
    total = len(labels)
    if total == 0:
        return 0.0
    cnt = Counter(labels)
    p = [count / total for count in cnt.values()]
    gini = 1 - sum(pi ** 2 for pi in p)
    return gini

# 找到标签
def label(idxs, y):
    labels = [y[i] for i in idxs]
    cnt = Counter(labels)
    max_count = max(cnt.values())
    return min(label for label, count in cnt.items() if count == max_count)

# 树的节点定义
class TreeNode:
    def __init__(self):
        self.is_leaf = True
        self.label = 0
        self.feature_index = -1
        self.threshold = 0.0
        self.left = None
        self.right = None


# 构建决策树
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

    # 遍历所有特征和切分点
    for feature_index in [0, 1]:
        for t in THRESHOLDS: # 直接用 t 作为切分点
            left_idxs = [i for i in idxs if X[i][feature_index] < t]
            right_idxs = [i for i in idxs if X[i][feature_index] >= t]

            if not left_idxs or not right_idxs: # 其中一边为空，不合理划分
                continue

            left_labels = [y[i] for i in left_idxs]
            right_labels = [y[i] for i in right_idxs]

            gini_left = gini_index(left_labels)
            gini_right = gini_index(right_labels)

            weighted_gini = (len(left_idxs) * gini_left + len(right_idxs) * gini_right) / len(idxs)

            # 更新条件
            # 1. gini 更小
            # 2. gini 相等时，选择特征索引更小的
            # 3. 特征索引也相等时，选择切分点更小的
            if weighted_gini < best_gini - 1e-12 or (abs(weighted_gini - best_gini) <= 1e-12 and (feature_index < best_feature or (feature_index == best_feature and t < (best_threshold if best_threshold is not None else 0)))):
                best_gini = weighted_gini
                best_feature = feature_index
                best_threshold = t
                best_left = left_idxs   
                best_right = right_idxs
    
    if best_left is None or best_gini >= curr_gini - 1e-12: # 无法划分或划分后更差
        node.is_leaf = True
        node.label = label(idxs, y)
        return node
    # 继续划分
    node.is_leaf = False
    node.feature_index = best_feature
    node.threshold = best_threshold
    node.left = build_tree(X, y, best_left, depth_limit - 1)
    node.right = build_tree(X, y, best_right, depth_limit - 1)
    return node

# 整个样本集的 Gini 系数，直接计算
train_labels = [y[i] for i in range(M)]
train_gini = gini_index(train_labels)
print(f"{train_gini:.4f}")

root = build_tree(X, y, list(range(M)), 5)

# 预测函数
def predict(sample, node):
    if node.is_leaf:
        return node.label
    if sample[node.feature_index] <= node.threshold:
        return predict(sample, node.left)
    else:
        return predict(sample, node.right)

predicted_label = predict(test_sample, root)
print(predicted_label)