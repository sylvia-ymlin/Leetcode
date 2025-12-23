# merge the overlapping intervals, and return a list that contains the merged intervals

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # input: 1 <= intervals.length <= 104
        # each element of intervals is a list of two integers

        # the problem is, can we assume the intervals are sorted? -> no

        return Solution1.merge(self, intervals)


# sorted
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # choose a nlogn sorting algorithm, such as quick sort or merge sort
        intervals.sort(key=lambda x: x[0])  # sort by the first element of each interval
        
        merged = []

        for interval in intervals:
            # since sorted, if merged is empty or the current interval does not overlap with the last merged interval, append it
            # directly append: if no interval in the merged list, or if the current interval starts after the last merged interval ends
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # since sorted, we only need to update the end of the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
# time compexlity: O(NlogN) for sorting, O(N) for merging, so overall O(NlogN)
# space complexity: O(N) for the merged list

# Sweep line algorithm
# 扫描线算法，将区间合并问题转换为事件处理问题
from collections import defaultdict
from typing import List
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)
        # 将每个区间的开始和结束位置作为事件
        for start, end in intervals:
            events[start] += 1   # 在start位置，活跃事件（区间）数+1
            events[end] -= 1     # 在end位置，活跃事件（区间）数-1
        
        # 存储合并区间
        res = []
        # 当前活跃区间
        interval = []
        have = 0 # 当前活跃事件（区间）数
        for i in sorted(events):  # 按位置从小到大处理所有事件
            if not interval:  # 如果当前没有活跃区间，开始一个新的区间
                interval.append(i) # 区间起始位置
            have += events[i]  # 更新当前位置的活跃区间数量
            # have will not be negative
            if have == 0: # 如果没有活跃区间，结束当前区间
                interval.append(i)
                res.append(interval)
                interval = [] # start a new interval
        return res

# time complexity: O(NlogN) for sorting the events, O(N) for processing the events, so overall O(NlogN)
# space complexity: O(N) for the events dictionary and the result list

# Greedy algorithm
# 贪心算法，直接遍历区间，合并重叠的区间
# time complexity: O(n + m)
# space complexity: O(m)
# m is the largest start value among the intervals, so this method is not efficient for large intervals
from typing import List
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 预处理：记录每个起始位置能延伸到的最远结束位置
        # 区间范围不会超过 max_val
        max_val = max(interval[0] for interval in intervals)
        # 闭区间，+1 表示刚好超出范围
        mp = [0] * (max_val + 1)
        for start, end in intervals:
            # 从 start开始，还可以延伸到 end + 1，
            # 取 Max，因为上位置的可延伸位置可能更远
            mp[start] = max(end + 1, mp[start])

        # 扫描合并区间
        res = [] # 存储合并的区间
        have = -1 # 当前"橡皮筋"能伸到的最远位置
        interval_start = -1  # 当前合并区间的起始位置
        for i in range(len(mp)): #遍历所有位置
            if mp[i] !=0: # 发现区间
                # the idea here is, if we find new interval before we reach the end of the current interval, the right interval bound will increase
                if interval_start == -1:  # 新区间，设置 start
                    interval_start = i
                have = max(have, mp[i])  # 更新当前活跃区间的结束位置
            if i == have:  # 到达当前区间结束位置
                res.append([interval_start, have])
                # 开启下一个合并区间
                interval_start = -1
                have = -1
        
        if interval_start != -1:  # 如果还有未结束的合并区间
            res.append([interval_start, have])

        return res