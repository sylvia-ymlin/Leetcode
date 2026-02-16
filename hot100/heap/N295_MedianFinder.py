# Max-Min Heap to maintain median
# Max heap stores the smaller half of numbers in data stream, heap top is largest, total k + (1)
# Min heap stores the larger half of numbers in data stream, heap top is smallest, total k 
# If k+1, stack top is median
# If k, average of two heap tops

import heapq
class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()
        # Median is min heap top, or queMax_[0], mid, -queMin_[0]
        

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        # Inserted number less than median
        if not queMin_ or num <= -queMin_[0]:
            # Insert into min heap
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_): # Unbalanced
                heapq.heappush(queMax_, -heapq.heappop(queMin_)) # Adjust, should insert into max heap
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))
        

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        # Odd number
        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        # Even number
        return (-queMin_[0] + queMax_[0]) / 2

