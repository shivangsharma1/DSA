from collections import deque
queue = deque()
visited = set()


def bfs(graph, visited, node):
    visited.add(node)
    queue.appendleft(node)
    while len(queue) != 0:
        element = queue.pop()
        print(element, end=" ")
        for adjacent in graph[element]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.appendleft(adjacent)




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

    bfs(graph, visited, 'A')