from collections import deque


def bfs(grid):
    queue = deque()
    visited = set()
    ROW, COL = len(grid), len(grid[0])
    length = 0

    #adding the first element index in queue and visited
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:

        for _ in range(len(queue)):
            r, c = queue.popleft()

            if r == ROW -1  and c == COL - 1:
                return length
            
            neighbour = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in neighbour:
                row_del, col_del = r + dr, c + dc

                if (min(row_del, col_del) < 0 or row_del == ROW or col_del == COL or grid[row_del][col_del] == 1 or (row_del, col_del) in visited):
                    continue

                visited.add((row_del, col_del))
                queue.append((row_del, col_del))
        length+=1













if __name__ == '__main__':
    grid  = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
    print(bfs(grid))