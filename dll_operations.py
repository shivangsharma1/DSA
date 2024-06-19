class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    
    def __init__(self):
        self.head = None

    def traverse_ll(self):
        if self.head is None:
            print("LL has no element")
            return 
        else:
            iterator = self.head
            while iterator is not None:
                print(str(iterator.data) , end="-->")
                iterator = iterator.next

    def insert_ll(self, data):
        node=Node(data)

        node.next=self.head
        if self.head is not None:
            self.head.prev = node
        
        self.head = node

    def delete_ll(self, delete_node):
        if self.head is None or delete_node is None:
            return 
        
        if self.head == delete_node:
            self.head=delete_node.next
        
        if delete_node.next is not None:
            delete_node.next.prev = delete_node.prev

        if delete_node.prev is not None:
            delete_node.prev.next = delete_node.next


dll_list1 = DoubleLL()
dll_list1.insert_ll(2)
dll_list1.insert_ll(4)
dll_list1.insert_ll(5)
dll_list1.insert_ll(10)
dll_list1.insert_ll(12)
print("Doubly Linked List After insertion of nodes")
dll_list1.traverse_ll()
dll_list1.delete_ll(dll_list1.head)
print("\n Doubly Linked List after deletion")
dll_list1.traverse_ll()
        
