# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None

        queue = deque()
        output = []

        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            output.append(temp)
        return output


        