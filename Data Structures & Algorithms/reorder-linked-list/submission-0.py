# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mid_node(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse_list(self,head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.mid_node(head)
        head2 = self.reverse_list(mid)

        while head2.next:


            nxt1 = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt1
            
            head = nxt1
            head2 = nxt2

    

        