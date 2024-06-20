class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def minValueNode(root):
    while root and root.left:
        root = root.left
    return root

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)

    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.left
        else:
            min_node = minValueNode(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)

    return root