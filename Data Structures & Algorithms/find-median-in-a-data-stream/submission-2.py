class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def addNum(self, num: int) -> None:
        if not self.maxHeap or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        self.rebalance()

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]
    
    def rebalance(self):
        if self.minHeap and len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if self.maxHeap and len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))