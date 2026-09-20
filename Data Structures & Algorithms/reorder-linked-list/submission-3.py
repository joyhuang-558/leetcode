# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow =  head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        #反转链表
        cur = second
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        first_head = head
        second_head = pre


        while second_head:
            first_next = first_head.next
            second_next = second_head.next

            first_head.next = second_head
            second_head.next = first_next

            first_head = first_next
            second_head = second_next
            

        
        