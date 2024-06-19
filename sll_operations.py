class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLL:
    def __init__(self):
        self.head = None

    def len_ll(self):
        counter = 0
        if self.head is None:
            return 0
        else:
            iterator = self.head
            while iterator != None:
                counter += 1
                iterator = iterator.next
        return counter

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_at_index(self, data, ind):
        count = 0
        iterator = self.head
        while iterator:
            if count == ind-1:
                node = Node(data, iterator.next)
                iterator.next=node
                break
            iterator= iterator.next
            count+=1

    def del_at_pos(self, idx):
        if idx==0:
            self.head = self.head.next
            return
        
        if idx>0 and idx<self.len_ll():
            print("insice")
            iterator = self.head
            count=0
            while iterator:
                if count == idx-1:
                    iterator.next= iterator.next.next
                    break
                iterator=iterator.next
                count+=1
                print(f"count {count}")
            


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iterator = self.head
        list_str = " "
        while iterator:
            list_str += str(iterator.data) + "-->"
            iterator = iterator.next
        print(list_str)


if __name__ == "__main__":
    list_1 = SingleLL()
    list_1.insert_at_begin(45)
    list_1.print()
    list_1.insert_at_begin(50)
    list_1.print()
    list_1.insert_at_begin(60)
    list_1.print()
    list_1.insert_at_end(46)
    list_1.print()
    list_1.insert_at_end(34)
    list_1.print()

    list_1.insert_at_index(37,2)
    list_1.print()
    list_1.insert_at_index(37,0)
    list_1.print()


    list_1.del_at_pos(2)
    list_1.print()

    list_1.del_at_pos(0)
    list_1.print()
