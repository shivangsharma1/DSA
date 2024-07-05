class Solution:
    def climbStairs(self, n: int) -> int:
        # hashmap = {}
        def dp(n, hashmap):
            if n == 1 or n == 2:
                return n

            if n in hashmap: return hashmap[n]

            hashmap[n] = dp(n-1, hashmap) + dp(n-2, hashmap)
            return hashmap[n]

        return dp(n, {})
