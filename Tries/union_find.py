class UnionFind:
    def __init__(self, n):  #n represents the nodes
        self.parent  = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = [i]
            self.rank[i] = 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]        
            p = self.parent[p]

        return p
    
    def union(self, n1, n2):
        p1, p2 = self.parent[n1], self.parent[n2]

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1

        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        return True
