def topological_sort(edges, n):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    #populate the list
    for s, d, in edges:
        adj[s].append(d)

    visited = set()
    order = []

    for node in adj.keys():
        dfs(node, visited, order, adj)

    order.reverse()
    return order


def dfs(node, visited, order, adj):
    if node in visited:
        return 
    
    visited.add(node)
    for neighbor in adj[node]:
        dfs(neighbor, visited, order, adj)

    order.append(node)