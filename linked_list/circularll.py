class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None

class cll:
    def __init__(self):
        self.last = None

    def insertatstart(self, data):
        newnode = Node(data)
        if self.last is None:
            self.last = newnode
            newnode.next = self.last

        else:
            newnode.next = self.last.next
            self.last.next = newnode
    
    def printLL(self):
        if self.last is None:
            return
        else:
            cur = self.last.next
            while True:
                print(cur.val, end="==>")
                if cur==self.last:
                    break
                cur = cur.next
        print()

    def deleteatstart(self):
        if self.last is None:
            return
        elif self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def search(self, key):
        if self.last is None:
            return None
        else:
            cur = self.last.next
            keynode = None
            while True:
                if cur.val == key:
                    keynode=cur
                    break
                if cur == self.last:
                    break
                cur = cur.next
            return keynode
        
    def insertatmid(self, posnode, data):
        newnode = Node(data)
        store = posnode.next
        posnode.next = newnode
        newnode.next = store





l = cll()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertatstart(i)

# l.printLL()
# l.deleteatstart()
# l.printLL()
key = 3
posnode = l.search(key)
print(posnode.val)
data = 10
l.insertatmid(posnode, 10)
l.printLL()