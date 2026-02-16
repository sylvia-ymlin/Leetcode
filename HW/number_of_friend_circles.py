# Count maximal cliques of size k >= 3
# Keywords: Undirected, Complete, Maximal -> Bron-Kerbosch algorithm
# Algorithm idea:
# 1. Recursively build candidate set P (vertices that can be added), current set R (vertices already added), excluded set X (vertices already excluded)
# 2. When P and X are both empty, R is a maximal clique
# 3. Use pivot to reduce recursion steps
# Hard to understand, just memorize code

# Number of relations

def friend_circles(): # Time complexity: O(3^(n/3))
    m = int(input())

    friends = {} # Name to index mapping
    relations = [] # Store relation pairs
    cnt = 0

    # Read relations
    for _ in range(m):
        a, b = input().replace(',', ' ').split()
        if a not in friends:
            friends[a] = cnt
            cnt += 1
        if b not in friends:
            friends[b] = cnt
            cnt += 1
        relations.append((friends[a], friends[b]))

    # Number of friends
    n = cnt

    # Build adjacency list
    adj = [set() for _ in range(n)]
    for u, v in relations:
        adj[u].add(v)
        adj[v].add(u)

    # Store maximal cliques
    maximal_cliques = []

    # Three sets
    # R: Current clique vertex set, all points in R are connected to each other
    # P: Candidate vertex set, all points in P are connected to every point in R
    # X: Points in X are also connected to every point in R, but have been used or excluded
    def bron_kerbosch(R, P, X):
        # When P and X are both empty, R is a maximal clique
        # P empty means no more vertices can be added to R while maintaining completeness
        # X empty means no previously skipped vertex exists that could theoretically be added to R; if X not empty, someone connects to all R, but we chose not to add them for now
        if not P and not X:
            if len(R) >= 3:
                maximal_cliques.append(R.copy())
            return
        
        # From union of P and X, pick a pivot u randomly
        u = next(iter(P | X)) if P | X else None # pivot speeds up, reduces recursion, removing it doesn't affect result correctness
        for v in P - adj[u] if u is not None else P: 
            # Choose to add v to R
            bron_kerbosch(
                R | {v}, # Union op, add v to R
                P & adj[v], # Intersection, generate new candidate set, keep only vertices connected to v
                X & adj[v]) # Intersection, previously tried points, if connected to v, keep in X, continue to judge; if not connected to v, definitely cannot join R, can be discarded
            # Undo selection, move v from P to X
            P.remove(v) # Remove v from P
            X.add(v) # Add v to X

    bron_kerbosch(set(), set(range(n)), set())
    print(len(maximal_cliques))

# Another simpler intuitive solution
# Enumerate all subsets of vertices with size >= 3, check if it is a clique

from collections import defaultdict
from itertools import combinations
def friend_circles_simple():
    m = int(input())
    graph = defaultdict(set) # Use adjacency list to store graph
    friends = set() # Store all friend names
    for _ in range(m):
        a, b = input().replace(',', ' ').split()
        graph[a].add(b)
        graph[b].add(a)
        friends.add(a)
        friends.add(b)
    
    friends = list(friends) # Convert to list for indexing
    find_cliques = []

    # Enumerate possible circle sizes, from small to large? No, code says len(friends) down to 2 ??
    # range(len(friends), 2, -1) means from N down to 3
    for size in range(len(friends), 2, -1):
        for group in combinations(friends, size): # Enumerate all combinations of size 'size'
            # Check if group is a clique
            is_clique = True
            for u, v in combinations(group, 2):
                if v not in graph[u]:
                    is_clique = False
                    break
            if is_clique:
                # Check if it is a subset of a larger clique found
                is_subset = False
                for existing in find_cliques:
                    if set(group).issubset(set(existing)):
                        is_subset = True
                        break
                if not is_subset:
                    find_cliques.append(group)
                    
    print(len(find_cliques))
            
if __name__ == "__main__":
    # friend_circles() # Time complexity: O(3^(n/3))
    friend_circles_simple() # Time complexity: O(n^2 * 2^n)
