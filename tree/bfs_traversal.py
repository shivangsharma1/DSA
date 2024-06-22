from collections import deque
def bsf(root):

    if not root:
        return None
    
    level = 0
    queue = deque()
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            print("level: ", level)
            curr = queue.popleft()
            print("rot value: ", curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        level+=1


