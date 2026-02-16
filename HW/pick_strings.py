# Given lowercase strings A and B
# A may contain duplicate letters, letters in B are unique
# Select some letters from A to form string B
# 1. Each letter at a position can only be selected once -> remove after selection
# 2. Relative order of selected letters cannot change (Constraint 3 in original text, numbering skipped 2)

# Output number of ways to pick letters from A to form B

# Continuously find each letter of B in A. After finding a group, remove corresponding letters (or move index), continue finding next group, until cannot find.
# Actually, this description seems to imply finding *disjoint subsequences*?
# "Select letters from A to form B... order cannot change" -> B is a subsequence of A.
# "Output number of ways... to form B" -> How many disjoint subsequences of A are equal to B?
# Original logic:
# `indices` stores indices of each char in A.
# Loop:
#   For each char in B:
#     Find first index of char in A that is > last_index.
#     If found, update last_index, remove index from list.
#     If not found, exit.
# This logic implements a greedy approach to find ONE subsequence, then remove it, then find NEXT.
# It counts how many *disjoint* copies of B can be formed from A, using a greedy strategy (taking earliest possible occurrences).
# Is greedy optimal for max number of disjoint subsequences?
# For example A = "ababa", B = "aba".
# Greedy:
# 1. 'a' at 0. 'b' at 1. 'a' at 2. Indices used {0, 1, 2}. Remainder "ba". Count = 1.
# Optimal? Maybe "aba" at 0,1,2 and "ba" at 3,4? No.
# Actually, greedy for subsequence usually works for checking existence.
# But for max number of disjoint subsequences?
# If B has unique characters (as stated: "B in letters are unique"), then the order is fixed unique chain.
# A = "a...b...c..."
# Since all chars in B are unique, picking the earliest 'a', then earliest 'b' after 'a', etc., is optimal for maximizing count.
# Because picking an earlier 'a' never hurts ability to pick 'b' later.
# So greedy strategy is correct because B has unique characters.

from collections import deque


a = input().strip()
b = input().strip()

# Record indices of each char in A
indices = {c: deque() for c in set(a)}
for i, c in enumerate(a):
    indices[c].append(i)

count = 0
while True:
    last_index = -1 # Record position of previous letter
    for c in b:
        if c not in indices:
            print(count)
            exit()
        # Find first position in indices[c] greater than last_index
        while indices[c] and indices[c][0] <= last_index:
            indices[c].popleft()
        if not indices[c]:
            print(count)
            exit()
        else:
            last_index = indices[c].popleft()
    # Successfully found one group of B, increment count
    count += 1

print(count)
