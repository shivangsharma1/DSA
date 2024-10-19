class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def find(self, x):
        if x not in self.parent: #default values for rank and parent - normally we just do it in init
            self.parent[x] = x
            self.rank[x] = 1
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, x, y):
        xx, yy = self.find(x), self.find(y)
        if xx == yy: # same parent means we're already connected.
            return False
        if self.rank[xx] > self.rank[yy]:
            self.parent[yy] = xx
        else:
            self.parent[xx] = yy
            self.rank[yy] += 1
        return True

def main(n):
    uf = DSU()
    all_nodes = set() # we would like to know just the unique combinations of nodes.
    for f, t in n:
        uf.union(f, t)
        all_nodes.add(f)
        all_nodes.add(t)
    
    all_nodes = list(all_nodes) 
    res = []
    for i in range(len(all_nodes)):
        for j in range(i+1,len(all_nodes)):
            if uf.find(all_nodes[i]) != uf.find(all_nodes[j]): # different parents = disconnected.
                res.append([all_nodes[i],all_nodes[j]])
    return res
print(main([(1,3),(2,7),(3,8)]))