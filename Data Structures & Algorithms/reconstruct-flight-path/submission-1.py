class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, dest in sorted(tickets)[::-1]:
            graph[source].append(dest)
        
        result = []
        def dfs(source):
            while graph[source]:
                dest = graph[source].pop()
                dfs(dest)
            result.append(source)
        
        dfs("JFK")
        return result[::-1]