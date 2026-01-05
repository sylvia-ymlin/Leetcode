# 对匹配结果去重
# 第一行输入有多少个匹配结果

# 有交集 -> 合并
# 并查集

class UnionFind:
    def __init__(self):
        self.parent = {} # 记录每个节点的父节点
    
    def find(self, x): # 找到根节点
        if self.parent[x] != x: # 不是自己，继续找父节点
            # 找父节点的同时进行路径压缩
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y): # 合并两个节点
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY: # 将其中一个根节点指向另一个根节点
            self.parent[rootY] = rootX # 将 y 的根节点指向 x 的根节点
    

def merge_matches(n, systems):
    uf = UnionFind()
    
    # 初始化: 对每个唯一实体初始化父节点为自己
    for line in systems:
        for entity in line:
            if entity not in uf.parent:
                uf.parent[entity] = entity
    
    # 按每行合并
    for line in systems:
        base = line[0]
        for entity in line[1:]:
            uf.union(base, entity) # 合并这两个实体所在的系统
    # 收集
    groups = {}
    # 遍历所有节点
    for entity in uf.parent:
        root = uf.find(entity) # 找到根节点
        groups.setdefault(root, set()).add(entity) # 将实体加入对应的根节点组中
    
    # 排序
    result = []
    for group in groups.values():
        result.append(sorted(group))
    result.sort()
    return result

# 输入处理
n = int(input().strip())
systems = []
for _ in range(n):
    line = input().strip().split()
    systems.append(line)

merged = merge_matches(n, systems)
for group in merged:
    print(" ".join(group))

