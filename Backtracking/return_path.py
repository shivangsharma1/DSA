class Node:
    def __init__(self , val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def rec(node, currentSum, path):
            if not node:
                return

            currentSum += node.val
            path.append(node.val)
            

            if currentSum == targetSum and not node.left and not node.right:
                result.append(list(path))
            else:
                rec(node.left, currentSum, path)
                rec(node.right, currentSum, path)

            path.pop()

        rec(root, 0, [])
        return result

# class Solution:
#     def pathSum(self, root, targetSum):
#         curpath, paths, cursum = [], [], 0

#         def dfs(root, curpath, paths, cursum):
#             if not root:
#                 return 

#             cursum+=root.val
#             curpath.append(root.val)

#             if cursum == targetSum and not root.left and not root.right:
#                 paths.append(curpath.copy)

#             dfs(root.left, curpath, paths, cursum)
#             dfs(root.right, curpath, paths, cursum)

#             curpath.pop()

#         dfs(root, curpath, paths, cursum)
#         return paths


root = Node(5)

root.left = Node(4)
root.right = Node(8)

root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)

root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

obj = Solution()
print(obj.pathSum(root, 22))