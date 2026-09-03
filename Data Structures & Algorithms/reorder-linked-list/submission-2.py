# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        h2  = self.reverse(h2)
        h1 = head
        while h2:
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2
            h2.next = temp1
            h1 = temp1
            h2 = temp2





    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre



        