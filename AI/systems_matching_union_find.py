# Deduplicate matching results
# First line inputs number of matching results

# Has intersection -> Merge
# Union Find

class UnionFind:
    def __init__(self):
        self.parent = {} # Record parent of each node
    
    def find(self, x): # Find root node
        if self.parent[x] != x: # Not self, continue finding parent
            # Path compression while finding parent
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y): # Merge two nodes
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY: # Point one root node to another root node
            self.parent[rootY] = rootX # Point y's root node to x's root node
    

def merge_matches(n, systems):
    uf = UnionFind()
    
    # Initialize: Initialize parent as self for each unique entity
    for line in systems:
        for entity in line:
            if entity not in uf.parent:
                uf.parent[entity] = entity
    
    # Merge by line
    for line in systems:
        base = line[0]
        for entity in line[1:]:
            uf.union(base, entity) # Merge systems these entities belong to
    # Collect
    groups = {}
    # Traverse all nodes
    for entity in uf.parent:
        root = uf.find(entity) # Find root node
        groups.setdefault(root, set()).add(entity) # Add entity to corresponding root node group
    
    # Sort
    result = []
    for group in groups.values():
        result.append(sorted(group))
    result.sort()
    return result

# Input processing
n = int(input().strip())
systems = []
for _ in range(n):
    line = input().strip().split()
    systems.append(line)

merged = merge_matches(n, systems)
for group in merged:
    print(" ".join(group))
