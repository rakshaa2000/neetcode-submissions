class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followee in self.followMap[userId]:
                if followee in self.tweetMap:
                    index = len(self.tweetMap[followee]) - 1
                    count, tweetId = self.tweetMap[followee][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followee, index-1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followee, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [count, tweetId, followee, index-1])
        else:
            for followee in self.followMap[userId]:
                if followee in self.tweetMap:
                    index =  len(self.tweetMap[followee]) - 1
                    count, tweetId = self.tweetMap[followee][index]
                    heapq.heappush(minHeap, [count, tweetId, followee, index-1])
        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)        

