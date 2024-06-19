# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2 ):
    add1, add2 = 0, 0
    while l1 or l2:
        if l1:
            add1 = l1.val*10 + add1
            l1 = l1.next

        if l2:
            add2 = l2.val*10 + add2
            l2 = l2.next

    addition = (add1//10)+(add2//10)

    dummy=ListNode()
    while  addition!=0:
        node = ListNode(addition%10)
        addition = addition//10
        if dummy.next is None:
            dummy.next = node
        else:
            node.next=node

    return dummy.next 


if __name__ == '__main__':
    l1 = ListNode(2)
    h1 = l1
    l1.next = ListNode(4)
    l1 = l1.next
    l1.next = ListNode(3)
    # l1 = [2,4,3]

    # l2 = [5,6,4]
    l2 = ListNode(5)
    h2 = l2
    l2.next = ListNode(6)
    l2=l2.next
    l2.next = ListNode(4)

    res = addTwoNumbers(h1, h2)
    


    # [7,0,8]
    # 342 + 465 = 807.