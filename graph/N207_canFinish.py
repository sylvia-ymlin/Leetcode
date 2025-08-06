# 需要所有节点都存在
# 有向图中没有环

# 但是官方题解给的标签是 拓扑排序
# 给定一个包含 n 个节点的有向图 G，给出它的节点编号的一种排列，如果满足：对于图 G 中的任意一条有向边 (u,v)，u 在排列中都出现在 v 的前面。称该排列是 G 的拓扑排序。

# 所以对这个问题，将课程视为节点，prerequisites 给出图中的有向边，我们要判断这个图是否存在拓扑排序

# 求出一种拓扑排序的最优时间复杂为 O(n+m)，其中 n 和 m 分别是有向图 G 的节点数和边数
# 所以本题至少需要对其完成一次遍历，不可能有更优算法

# 深度优先
# 对于一个节点 u，如果它的所有相邻节点都已经搜索完成，那么在搜索回溯到 u 的时候，u 本身也会变成一个已经搜索完成的节点。这里的「相邻节点」指的是从 u 出发通过一条有向边可以到达的所有节点。
# 假设我们当前搜索到了节点 u，如果它的所有相邻节点都已经搜索完成，那么这些节点都已经在栈中了，此时我们就可以把 u 入栈。可以发现，如果我们从栈顶往栈底的顺序看，由于 u 处于栈顶的位置，那么 u 出现在所有 u 的相邻节点的前面。因此对于 u 这个节点而言，它是满足拓扑排序的要求的。
# 这样以来，我们对图进行一遍深度优先搜索。当每个节点进行回溯的时候，我们把该节点放入栈中。最终从栈顶到栈底的序列就是一种拓扑排序。

# 图中任意一个节点，它在搜索的过程中有三种状态
# 「未搜索」：我们还没有搜索到这个节点；
# 「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成）；
# 「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求。

# 我们将当前搜索的节点 u 标记为「搜索中」，遍历该节点的每一个相邻节点 v：

# 如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；

# 如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；

# 如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，因此 u 无论何时入栈都不会影响到 (u,v) 之前的拓扑关系，以及不用进行任何操作。

# 当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。

# 所以，有环的状态就是，在搜索中遇到处于搜索中的节点

from typing import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1 # 探索中
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i) # 遍历所有没有遍历的点
        
        return valid