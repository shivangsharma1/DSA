import heapq

def min_spanningtree(edges, n):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    # populate the adj list
    for s, d, w in edges:
        adj[s].append((w, d))
        adj[d].append((w, s))

    minheap = []
    mst = []
    visited = set()
    for w, d in adj[1]:
        heapq.heappush(minheap, (w, 1, d))

    visited.add(1)

    while minheap:
        w, s ,node = heapq.heappop(minheap)
        if node in visited:
            continue

        mst.append((s, node))
        visited.add(node)

        for w, neigh in adj[node]:
            if neigh not in visited:
                heapq.heappush(minheap, (w, node, neigh))

    return mst