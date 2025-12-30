# 智能客户分群与新用户定位(KMeans均衡分区版)

# 使用 K-means 变种聚类，将用户划分为 k 个群组，且保证每个群组人数相差不超过1
# 当人数无法均分，将多出来的客户分配给聚类中心编号更小的群组，分配唯一
# 新客户数据，利用最终分群中心点分配合适的群组

# 输入：N 位客户，每位客户有 M 个特征
# 分群个数，（2 <= k <= min(20, N)）
# 初始聚类中心：输入的前 k 位客户
# 聚类算法流程：
# 1. 根据输入顺序，依次处理每个客户
# 2. 计算客户与各聚类中心的欧氏距离，选择距离最近的聚类中心，相同时选最小
# 3. 检查该聚类中心对应的群组人数是否已达上限，若未达上限则分配该群组，若已达上限则选择下一个距离最近的聚类中心，重复步骤3
# 4. 多余的顾客分配给编号更小的群组
# 5. 第一轮分配结束后，更新聚类中心为各群组内客户的均值 （向下取整）
# 6. 重复步骤1-5，直到聚类中心不再变化

# 给出一个新客户的数据


# 输出每个中心点的特征值
# 输出新用户的群组编号 (从 1 开始)

# 计算欧氏距离
def euclidean_distance(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(m))

# 更新聚类中心
def update_centers(groups):
    new_centers = []
    for group in groups:
        new_center = [sum(customer[j] for customer in group) // len(group) for j in range(m)]
        new_centers.append(new_center)
    return new_centers

# 返回最近的群组索引
def find_closest_groups(customer, centers, groups):
    distances = [(euclidean_distance(customer, centers[j]), j) for j in range(len(centers))]
    # 按距离升序，编号升序排序
    distances.sort(key=lambda x: (x[0], x[1]))
    for _, group_idx in distances:
        if len(groups[group_idx]) < MAX_SIZE[group_idx]:
            return group_idx
    # 全满了
    return distances[0][1]

# 第一行，N, M, k
n, m, k = map(int, input().strip().split())
# 读入客户数据
data = [list(map(int, input().strip().split())) for _ in range(n)]
# 读入新客户数据
new_customer = list(map(int, input().strip().split()))

if n < k:
    k = n

# 给每个组设置最大容量
MAX_SIZE = [n // k] * k
for i in range(n % k):
    MAX_SIZE[i] += 1

groups = []
for i in range(k):
    groups.append([data[i]])  # 初始化每个群组，放入初始中心点

# 初始化聚类中心
centers = data[:k]

# 第一轮
for i in range(k, n):
    customer = data[i]
    group_id = find_closest_groups(customer, centers, groups)
    groups[group_id].append(customer)

# 迭代更新聚类中心和分配群组
while True:
    new_centers = update_centers(groups)
    if new_centers == centers:
        break
    centers = new_centers
    # 清空群组，重新分配
    groups = [[] for _ in range(k)]
    for i in range(n):
        customer = data[i]
        group_id = find_closest_groups(customer, centers, groups)
        groups[group_id].append(customer)

# 对最终的群组按照聚类中心排序
centers.sort()
# 输出最终聚类中心
for center in centers:
    print(' '.join(map(str, center)))

# 分配新客户，直接计算
_, new_group_id = min((euclidean_distance(new_customer, centers[j]), j) for j in range(k))
print(new_group_id + 1)


    