# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.out = []
    
    def inorder(self,root):  
        if not root: return None
        
        self.inorder(root.left)
        self.out.append(root.val)
        self.inorder(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        self.inorder(root)
        return self.out[k-1]
        