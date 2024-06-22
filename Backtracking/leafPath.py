class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leafPath(root, path):
    if not root or root.val == 0:
        return False 
    
    path.append(root.val)

    if not root.left and not root.right:
        return True
    
    if leafPath(root.left, path):
        return True
    
    if leafPath(root.right, path):
        return True
    
    path.pop()
    return False


def canreachleaf(root):

    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    
    if canreachleaf(root.left):
        return True
    
    if canreachleaf(root.right):
        return True
    
    return False