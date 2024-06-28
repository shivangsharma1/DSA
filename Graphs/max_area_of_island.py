from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))
            area = 1

            while q:
                r, c = q.popleft()

                neighbour = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in neighbour:
                    del_r, del_c = r+dr, c+dc
                    if min(del_r, del_c) < 0 or del_r == ROW or del_c == COL or grid[del_r][del_c] == 0 or (del_r, del_c) in visited:
                        continue
                    area+=1
                    visited.add((del_r, del_c))
                    q.append((del_r, del_c))

            return area


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c) 
                    max_area = max(area, max_area)

        return max_area