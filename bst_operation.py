class BSTNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def insert_BST(root, data):
    if root is None:
        return BSTNode(data)
    
    else:
        if root.val == data:
            return root
        elif data > root.val:
            root.right = insert_BST(root.right, data)
        else:
            root.left = insert_BST(root.left, data)

        return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def search_bst(root, data):
    while root!=None:
        if data < root.val:
            return search_bst(root.left, data)
        elif data > root.val:
            return search_bst(root.right, data)
        else:
            return print("True")
    return print("False")

def find_min_node(node):
    cur = node
    while cur.left!=None:
        cur=cur.left

    return cur

def deleteNode(root, data):
    if root is None:
        return root
    
    if data > root.val:
        root.right = deleteNode(root.right, data)

    elif data < root.val:
        root.left = deleteNode(root.left, data)

    else:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        ## when both child nodes are present

        min_node = find_min_node(root.right)

        root.val = min_node.val

        root.right = deleteNode(root.right, min_node.val)

    return root

if __name__ =='__main__':
    r = BSTNode(50)
    r = insert_BST(r, 30)
    r = insert_BST(r, 20)
    r = insert_BST(r, 40)
    r = insert_BST(r, 70)
    r = insert_BST(r, 60)
    r = insert_BST(r, 80)

    # search_bst(r, 90)
    inorder(r)
    deleteNode(r, 30)
    print()
    inorder(r)