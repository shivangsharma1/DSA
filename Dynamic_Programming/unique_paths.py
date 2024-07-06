class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r, c, row, col, cache):
            #memoization technique
            if r>=row or c>=col: 
                return 0
            if cache.get((r, c), 0)>0: 
                return cache[(r, c)]
            if r==row-1 and c==col-1: 
                return 1

            cache[(r, c)] = dp(r+1, c, row, col, cache) + dp(r, c+1, row, col, cache)

            return cache[(r, c)]

        return dp(0, 0, m, n, {})

