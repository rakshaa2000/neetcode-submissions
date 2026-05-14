from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                # +1 as it is a maxHeap and numbers are in negative, don't get confused
                tasksRemaining = 1 + heapq.heappop(maxHeap)
                if tasksRemaining:
                    q.append([tasksRemaining, time + n])
            
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
