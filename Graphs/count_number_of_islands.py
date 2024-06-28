class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                r, c = q.popleft()
                neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in neighbours:
                    del_r, del_c= r+dr, c+dc

                    if (min(del_r, del_c) < 0 or del_r == ROW or del_c == COL or grid[del_r][del_c] == "0" or (del_r, del_c) in visited):
                        continue
                    visited.add((del_r, del_c))
                    q.append((del_r, del_c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands+=1

        return num_islands