class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert_at_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def del_from_start(self):
        if self.head is None:
            return
        self.head = self.head.next

    def insert_at_end(self, val):
        if self.head is None:
            return self.insert_at_start(val)
        
        cur = self.head
        while cur.next:
            cur = cur.next
        newnode = Node(val)
        cur.next = newnode

    def println(self):
        if self.head is None:
            return None
        cur = self.head
        while cur:
            print(cur.val)
            print("==>")
            cur=cur.next





l = LL()
li = [1,2,3,4,5]
for i in li:
    l.insert_at_start(i)
l.insert_at_end(10)
l.println()








