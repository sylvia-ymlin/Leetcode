"""
2025-10-22 L5

Word Chain, splice words, take longest for same starting letter, return lexicographically smallest for same length
"""

import sys

def main():
    start = int(input())
    n = int(input())
    # Word list
    words = [sys.stdin.readline().strip() for _ in range(n)]

    cur = words[start]
    ans =  [[] for _ in range(26)] # Store words

    for i in range(n):
        if i != start:
            idx = ord(words[i][0]) - ord('a')
            ans[idx].append(words[i])
    
    # For same starting letter, sort by length descending first, then by lexicographical order ascending
    for i in range(n):
        ans[i].sort(key=lambda x: (-len(x), x))
    
    res = cur
    while cur:
        idx = ord(cur[-1]) - ord('a')
        if len(ans[idx]) > 0:
            cur = ans[idx].pop(0)
            res += cur
        else:
            break
    
    print(res)
    

if __name__ == "__main__":
    from io import StringIO
    import sys

    input_data = """0
                6
                word
                dd
                da
                dc
                dword
                d"""
    expected_output = "worddwordda"
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    main()
    output = sys.stdout.getvalue().strip()
    assert output == expected_output, f"Expected: {expected_output}, but got: {output}"
    print("Test passed.")