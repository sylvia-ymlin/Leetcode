# 统计 k >= 3 的极大完全子图
# 三个关键词：无向、完全、极大 -> bron-kerbosch 算法
# 算法思想：
# 1. 递归地构建候选集合 P（可能加入的顶点）、当前集合 R（已经加入的顶点）、排除集合 X（已经排除的顶点）
# 2. 当 P 和 X 都为空时，R 就是一个极大完全子图
# 3. 通过选择 pivot 来减少递归次数
# 有点难理解，记住代码即可


# 多少条关系

def friend_circles(): # 时间复杂度：O(3^(n/3))
    m = int(input())

    friends = {} # 名字到索引的映射
    relations = [] # 存储关系对
    cnt = 0

    # 读取关系
    for _ in range(m):
        a, b = input().replace(',', ' ').split()
        if a not in friends:
            friends[a] = cnt
            cnt += 1
        if b not in friends:
            friends[b] = cnt
            cnt += 1
        relations.append((friends[a], friends[b]))

    # 朋友个数
    n = cnt

    # 构建邻接表
    adj = [set() for _ in range(n)]
    for u, v in relations:
        adj[u].add(v)
        adj[v].add(u)

    # 存储极大完全子图
    maximal_cliques = []

    # 有三个集合
    # R: 当前完全子图的顶点集合，R 中的点两两相连
    # P: 可能加入的顶点集合，P 中的点和 R 中的每个点都相连
    # X: X 中的点也和 R 中每个点相连，但已经被用过或排除
    def bron_kerbosch(R, P, X):
        # 当 P 和 X 都为空时，R 是一个极大完全子图
        # P 为空表示，没有更多的顶点可以添加到 R 中而保持完全性
        # x 为空表示，不存在一个之前被跳过、但理论上还能加入 R 的人；如果 X 不为空，有人和 R 全员相连，但我们选择暂时不加他
        if not P and not X:
            if len(R) >= 3:
                maximal_cliques.append(R.copy())
            return
        
        # 从 P 和 X 的并集中，随机挑一个点作为 pivot u
        u = next(iter(P | X)) if P | X else None # pivot 用于加速，减少递归次数，直接删除不影响代码结果
        for v in P - adj[u] if u is not None else P: 
            # 选择将 v 加入 R
            bron_kerbosch(
                R | {v}, # 并集操作，将 v 加入 R
                P & adj[v], # 取交集，生成新的候选集，只留下和 v 相连的顶点
                X & adj[v]) # 取交集，之前已经尝试过的点，如果和 v 相连，继续保留在 X 中，需要继续判断；如果不和 v 相连，一定不能加入 R，可以直接丢弃
            # 撤销选择，将 v 从 P 移到 X
            P.remove(v) # 从 P 中移除 v
            X.add(v) # 将 v 加入 X

    bron_kerbosch(set(), set(range(n)), set())
    print(len(maximal_cliques))

# 另一个比较简单直观的解法
# 枚举所有大小 >= 3 的顶点子集，判断是否为完全子图

from collections import defaultdict
from itertools import combinations
def friend_circles_simple():
    m = int(input())
    graph = defaultdict(set) # 使用邻接表存储图
    friends = set() # 存储所有朋友的名字
    for _ in range(m):
        a, b = input().replace(',', ' ').split()
        graph[a].add(b)
        graph[b].add(a)
        friends.add(a)
        friends.add(b)
    
    friends = list(friends) # 转换为列表以便索引
    find_cliques = []

    # 从小到大，枚举朋友圈可能的大小
    for size in range(len(friends), 2, -1):
        for group in combinations(friends, size): # 枚举所有大小为 size 的组合
            # 判断 group 是否为完全子图
            is_clique = True
            for u, v in combinations(group, 2):
                if v not in graph[u]:
                    is_clique = False
                    break
            if is_clique:
                # 判断是否是某个更大完全子图的子集
                is_subset = False
                for existing in find_cliques:
                    if set(group).issubset(set(existing)):
                        is_subset = True
                        break
                if not is_subset:
                    find_cliques.append(group)
                    
    print(len(find_cliques))
            
if __name__ == "__main__":
    # friend_circles() # 时间复杂度：O(3^(n/3))
    friend_circles_simple() # 时间复杂度：O(n^2 * 2^n)
