class UnionFind:
    parent = {}
    connected = 0
    def __init__(self, n):
        self.connected = n
        self.parent = {i: i for i in range(n)}
    def find(self, x):
        while (self.parent[x] != x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        self.connected -= 1
        self.parent[rootY] = rootX
        return True
    def connectedComponents(self):
        return self.connected

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist, i, j])
        edges.sort()
        uf = UnionFind(len(points))
        cost = 0
        for edge in edges:
            connect = uf.union(edge[1], edge[2])
            if connect:
                cost += edge[0]
        return cost if uf.connectedComponents() == 1 else -1