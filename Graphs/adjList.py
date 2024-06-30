from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbor = []

def dfs(node, target, adjList, visited):
    if node in visited:
        return 0
    
    if node == target:
        return 1
    
    count=0
    visited.add(node)
    for neigh in adjList[node]:
        count+=dfs(neigh, target, adjList, visited)\
        
    return count

def bfs(node, target, adjList):
    # length = 0
    visited = set()
    q = deque()
    visited.add(node)
    q.append((node, 1))

    while q:
        cur, length = q.popleft()
        if cur == target:
            return length
        
        for neighbor in adjList[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, length+1))

    return length

adjList = {}
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"],["E", "D"]]

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

print("adjList:", adjList)

print("DFS : all paths: ", dfs("A", "E", adjList, set()))

print("BFS : shortest: ", bfs("A", "E", adjList))
