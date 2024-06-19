class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None

    def insertatend(self, data):
        newnode = Node(data)
        cur = self.head
        if self.head == None:
            self.head = newnode

        else:
            while cur.next!=None:
                cur = cur.next
            cur.next = newnode
            newnode.prev = cur

    def printLL(self):
        cur = self.head
        while cur:
            print(cur.val, end = "==>")
            cur = cur.next
        print()

    def deleteatstart(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None

    def insertatmid(self, data, curnode):
        newnode = Node(data)
        store = curnode.next
        curnode.next = newnode
        newnode.next = store
        newnode.prev = curnode
        store.prev = newnode

    def search(self, nodeval):
        cur = self.head
        while cur != None:
            if cur.val == nodeval:
                return_node = cur
                break
            cur = cur.next

        return return_node

    def deleteatmid(self, nodetodel):
        cur = self.head
        if cur is None or cur.val == nodetodel: 
            return None
        prev = nodetodel.prev
        prev.next = nodetodel.next
        nodetodel.next.prev = prev



l = Dll()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertatend(i)
l.printLL()
node = l.search(3)
l.deleteatmid(node)
l.printLL()