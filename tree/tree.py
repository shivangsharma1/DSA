class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    

    def insertnode(self, root ,val):
        if self.root is None:
            return Node(val)
        
        else:
            cur = self.root
            if cur.val == val:
                return
            elif val> cur.val:
                cur.right = self.insertnode(cur.right, val)
            else:
                cur.left = self.insertnode(cur.left, val)


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)



t = BST()
nodes = [6,8, 7, 9, 4, 3, 5]
a = Node(6)
for val in nodes:
    t.insertnode(None,val)

t.inorder(a)

