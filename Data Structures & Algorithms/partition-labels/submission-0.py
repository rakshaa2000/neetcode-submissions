class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for i, ch in enumerate(s):
            lastSeen[ch] = i
        result = []
        size = end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, lastSeen[ch])
            if i == end:
                result.append(size)
                size = 0
        return result