class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        coursemap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            coursemap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if coursemap[crs] == []:
                return True

            visited.add(crs)
            for pre in coursemap[crs]:
                if not dfs(pre): return False

            visited.remove(crs)
            coursemap[crs] = []
            return True 

        for i in coursemap.keys():
            if not dfs(i): return False

        return True