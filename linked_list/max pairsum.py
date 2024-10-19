# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        #reversing the ll
        prev=None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt

        maxsum = 0
        while prev and l1 :
            print(f"prev val : {prev.val}")
            print(f"l1 val : {l1.val}")
            maxsum = max(l1.val+l2.val, maxsum)
            print(f"max : {maxsum}")
            l1=l1.next
            prev=prev.next
        return maxsum
        

arr = [5,4,2,1]
head = ListNode(5)
dummy = head
dummy.next = ListNode(4)
dummy = dummy.next
dummy.next = ListNode(2)
dummy = dummy.next
dummy.next = ListNode(1)

obj = Solution()
obj.pairSum(head)