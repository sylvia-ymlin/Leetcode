# 大小堆维护中位数
# 大堆中是数据流中最小的一半数，堆顶最大，一共 k + (1)
# 小堆中是数据流中最大的一半数，堆顶最小， 一共 k 
# 如果 k+1, 栈顶就是中位数
# 如果 k，两个堆顶取平均数

import heapq
class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()
        # 中位数为最小堆栈顶，或者  queMax_[0], mid, -queMin_[0]
        

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        # 插入的数小于中位数
        if not queMin_ or num <= -queMin_[0]:
            # 插入最小堆
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_): # 不平衡了
                heapq.heappush(queMax_, -heapq.heappop(queMin_)) # 调整，应该插入最大堆
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))
        

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        # 奇数个
        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        # 偶数个
        return (-queMin_[0] + queMax_[0]) / 2

