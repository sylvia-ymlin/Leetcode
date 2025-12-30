# 终端款型聚类识别
# 根据终端的特征，识别终端型号

# 四个特征：包间隔时长、连接持续时长、漫游前信号强度、漫游后信号轻度
# 终端有 k 类
# 使用 k-means 聚类算法进行识别

# 不存在某一类终端为 0
# 输入数据已完成归一化

# 初始 k 个质心为前 k 个样本点

def distance(a, b):
    """计算两个样本点之间的欧氏距离"""
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

# 终止条件：质心不再变化或达到最大迭代次数

k, m, n = map(int, input().split())

data = [list(map(float, input().split())) for _ in range(m)]

# 初始化质心
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

# 按照终端数量从小到大排序
counts = [len(cluster) for cluster in clusters]
counts.sort()
print(' '.join(map(str, counts)))