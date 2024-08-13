import heapq

def dijkstra(edges, n, source):
    
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    for s, d, w, in edges:
        adj[s].append((d, w))

    shortest = {}
    minheap = [(0, source)]

    while minheap:
        w1, n1 = heapq.heapop(minheap)
        if n1 in shortest:
            continue

        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minheap, (w1+w2, n2))

    return shortest

