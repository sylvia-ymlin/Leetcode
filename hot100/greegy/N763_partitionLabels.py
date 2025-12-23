# 同一个字母最多出现在一个片段里面
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 分析时间复杂度，最少需要遍历一次 O(N)

        # 第一次遍历，找到每个字母最后一次出现的下标
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        # 维护当前 valid 子串
        start = end = 0
        for i, ch in enumerate(s):
            # 当前字母 加入
            end = max(end, last[ord(ch) - ord("a")])
            if i == end: # 没有破坏当前序列合法性
                partition.append(end - start + 1)
                # 下一子序列
                start = end + 1
        
        return partition
