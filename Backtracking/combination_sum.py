class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i, subset, total):
            if i>=len(candidates) or total>target:
                return

            if total == target:
                res.append(subset.copy())
                return

            subset.append(candidates[i])
            dfs(i, subset, total + candidates[i])
            subset.pop()
            dfs(i+1, subset, total)

        dfs(0, subset, 0)
        return res
                