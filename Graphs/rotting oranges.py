class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rotten, fresh, time = 0, 0, 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotten+=1
                if grid[i][j] == 1:
                    fresh+=1
        
        while q and fresh>0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    del_r, del_c = r+dr, c+dc
                    if del_r in range(ROW) and del_c in range(COL) and grid[del_r][del_c] == 1:

                        grid[del_r][del_c]= 2
                        q.append((del_r, del_c))
                        fresh-=1


            time+=1
        return time if fresh == 0 else -1

        