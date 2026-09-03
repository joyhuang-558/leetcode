# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #这个是node，不是list
        l1 = list1
        l2 = list2
        #要用一个dummy来存头节点，最后返回dummy next
        dummy = ListNode()
        rs = dummy
        while l1 and l2:
            if l1.val < l2.val:
                rs.next = l1
                l1 = l1.next
                rs = rs.next
            else:
                rs.next = l2
                l2 = l2.next
                rs = rs.next
        rs.next = l1 or l2
        return dummy.next



        