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
# Sweep line algorithm
# Sweep line algorithm, convert interval merging problem to event processing problem
from collections import defaultdict
from typing import List
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)
        # Use start and end position of each interval as event
        for start, end in intervals:
            events[start] += 1   # At start, active events (intervals) +1
            events[end] -= 1     # At end, active events (intervals) -1
        
        # Store merged intervals
        res = []
        # Current active interval
        interval = []
        have = 0 # Current active events (intervals) count
        for i in sorted(events):  # Process all events from small to large
            if not interval:  # If no active interval, start a new one
                interval.append(i) # Interval start
            have += events[i]  # Update active interval count
            # have will not be negative
            if have == 0: # If no active interval, end current interval
                interval.append(i)
                res.append(interval)
                interval = [] # start a new interval
        return res

# time complexity: O(NlogN) for sorting the events, O(N) for processing the events, so overall O(NlogN)
# space complexity: O(N) for the events dictionary and the result list

# Greedy algorithm
# Greedy algorithm, directly traverse intervals, merge overlapping intervals
# time complexity: O(n + m)
# space complexity: O(m)
# m is the largest start value among the intervals, so this method is not efficient for large intervals
from typing import List
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Preprocessing: record the furthest end position each start position can reach
        # Interval range will not exceed max_val
        max_val = max(interval[0] for interval in intervals)
        # Closed interval, +1 means just out of range
        mp = [0] * (max_val + 1)
        for start, end in intervals:
            # From start, can reach end + 1,
            # Take Max, because extendable position from upper position can be further
            mp[start] = max(end + 1, mp[start])

        # Scan to merge intervals
        res = [] # Store merged intervals
        have = -1 # Furthest position current "rubber band" can reach
        interval_start = -1  # Start position of current merged interval
        for i in range(len(mp)): # Traverse all positions
            if mp[i] !=0: # Found interval
                # the idea here is, if we find new interval before we reach the end of the current interval, the right interval bound will increase
                if interval_start == -1:  # New interval, set start
                    interval_start = i
                have = max(have, mp[i])  # Update end position of current active interval
            if i == have:  # Reached end of current interval
                res.append([interval_start, have])
                # Start next merged interval
                interval_start = -1
                have = -1
        
        if interval_start != -1:  # If there is still unfinished merged interval
            res.append([interval_start, have])

        return res