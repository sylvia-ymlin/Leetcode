"""
2025-10-22 L4

给出自行车限重和部门总人数，求最多需要多少车
先排序，贪心
"""

import sys

def main():
    m, n = map(int, sys.stdin.readline().strip().split())
    weights = list(map(int, sys.stdin.readline().strip().split()))
    weights.sort()

    left, right = 0, n - 1
    res = 0
    while left <= right:
        if weights[left] + weights[right] <= m:
            left += 1
            right -= 1
        else:
            right -= 1
        res += 1
    
    print(res)

if __name__ == "__main__":
    main()
