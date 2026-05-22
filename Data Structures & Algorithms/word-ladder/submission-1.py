import heapq

class Solution:
    def possibleNext(self, start: str, word_set: set) -> list[str]:
        result = []
        for st in word_set:
            if len(st) != len(start):
                continue
            
            diff = 0
            for i in range(len(st)):
                if start[i] != st[i]:
                    diff += 1
                if diff > 1:
                    break
                    
            if diff == 1:
                result.append(st)
        return result

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        if beginWord == endWord:
            return 0

        graph = {}
        for word in word_set:
            graph[word] = self.possibleNext(word, word_set)
        graph[beginWord] = self.possibleNext(beginWord, word_set)
        
        q = [(1, beginWord)]
        
        minDist = {beginWord: 1}
        
        while q:
            step, front = heapq.heappop(q)
            
            if front == endWord:
                return step
                
            neighbours = graph.get(front, [])
            if not neighbours:
                continue
                
            for adj in neighbours:
                if adj not in minDist or minDist[adj] > step + 1:
                    minDist[adj] = step + 1
                    heapq.heappush(q, (step + 1, adj))
                    
        return 0