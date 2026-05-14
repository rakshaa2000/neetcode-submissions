class UnionFind:
    connected = 0
    parent = {}
    def __init__(self, n):
        self.connected = n
        self.parent = {i: i for i in range(n)}
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.connected -= 1
        self.parent[rootY] = rootX
        return True
    def components(self):
        return self.connected

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            connect = uf.union(edge[0], edge[1])
            if not connect:
                return False
        return uf.components() == 1