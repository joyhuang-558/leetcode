# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self,list1,list2):
        head = dummy = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        elif m == 1:
            return lists[0]
        else:
            left = self.mergeKLists(lists[:m//2])
            right = self.mergeKLists(lists[m//2:])
            return self.mergeTwoLists(left,right)
        