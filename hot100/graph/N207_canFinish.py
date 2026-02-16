# Need all nodes to exist
# No cycle in directed graph

# But official solution tag is Topological Sort
# Given a directed graph G with n nodes, give a permutation of its node numbers, if satisfied: for any directed edge (u,v) in graph G, u always appears before v in the permutation. This permutation is called topological sort of G.

# So for this problem, treating courses as nodes, prerequisites gives directed edges in graph, we need to determine if topological sort exists for this graph

# Optimal time complexity for finding a topological sort is O(n+m), where n and m are number of nodes and edges in directed graph G respectively
# So this problem requires at least one traversal, no better algorithm possible

# Depth First Search
# For a node u, if all its adjacent nodes have been searched, then when search backtracks to u, u itself becomes a searched node. "Adjacent nodes" here refer to all nodes reachable from u via a directed edge.
# Suppose we currently searched to node u, if all its adjacent nodes have been searched, then these nodes are already in stack, now we can push u into stack. We can find that, if looking from top to bottom of stack, since u is at top position, u appears before all its adjacent nodes. Thus for node u, it satisfies topological sort requirements.
# In this way, we perform DFS on graph once. When each node backtracks, we push it into stack. Finally sequence from stack top to bottom is a topological sort.

# Any node in graph has three states during search process
# "Unsearched": we haven't searched this node yet;
# "Searching": we searched this node, but haven't backtracked to it yet, i.e., this node hasn't been pushed to stack, adjacent nodes haven't finished searching);
# "Completed": we searched and backtracked this node, i.e., this node pushed to stack, and all adjacent nodes of this node appear at lower positions in stack, satisfying topological sort.

# We mark currently searched node u as "Searching", traverse every adjacent node v of this node:

# If v is "Unsearched", we start searching v, wait for search complete and backtrack to u;

# If v is "Searching", then we found a cycle in graph, thus topological sort doesn't exist;

# If v is "Completed", means v is already in stack, and u is not in stack yet, thus u pushed to stack anytime won't affect topological relation before (u,v), and no operation needed.

# When all adjacent nodes of u are "Completed", we push u to stack, and mark it as "Completed".

# So, cycle state is encountering a node in "Searching" state during search

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
            visited[u] = 1 # Searching
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
                dfs(i) # Traverse all unvisited points
        
        return valid