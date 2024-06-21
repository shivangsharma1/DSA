class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(root.append)
                cur = cur.left
            
            cur = stack.pop()
            n+=1
            if n==k:
                return cur.val
            
            cur = cur.right