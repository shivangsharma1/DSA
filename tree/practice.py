from collections import deque

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def search(root, val):
    if not root:
        return False

    if val > root.val:
        return search(root.right, val)
    elif val < root.left:
        return search(root.left, val)
    else:
        return True


def insert(root, val):
    if not root:
        return Node(val=val)

    if val > root.val:
        root.right = insert(root.right, val=val)
    else:
        root.left = insert(root.left, val=val)

    return root


def minvalueNode(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur


def remove(root, val):
    if not root:
        return

    # first search the val
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # now found the value, need to remove the value
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            # find min values
            minvalue = minvalueNode(root.right)
            root.val = minvalue
            root.right = remove(root.right, minvalue)

    return root


# DFS and BFS algo


def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return None

    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)

# TC: O(n)
def bfs(root):
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    level = 0
    while len(queue)>0:
        print(level) # if level information is needed

        for _ in range(len(queue)):
            cur = queue.pop()
            #if need to print the node values level wise print here the node value

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

        level+=1


