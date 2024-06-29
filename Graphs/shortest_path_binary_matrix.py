class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visited = set()
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        q.append((0, 0, 1))
        visited.add((0, 0))

        while q:
            r, c, length = q.popleft()

            if r not in range(ROW) or c not in range(COL) or grid[r][c]:
                continue

            if r == ROW-1 and c == COL-1:
                return length

            for dr, dc in direction:
                del_r, del_c = r+dr, c+dc
                if (del_r, del_c) not in visited:
                    visited.add((del_r, del_c))
                    q.append((del_r, del_c, length+1))

        return -1

