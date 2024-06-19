def dfs(graph, visited, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for adjacent in graph[node]:
            dfs(graph, visited, adjacent)





if __name__ == '__main__':
    graph = {
        'A' : ['B','C','D'],
        'B' : ['E'],
        'C' : ['E', 'F'],
        'D' : ['F'],
        'E' : ['G'],
        'F' : ['G'],
        'G' : [], 
    }
    visited = set()
    dfs(graph, visited ,'A')