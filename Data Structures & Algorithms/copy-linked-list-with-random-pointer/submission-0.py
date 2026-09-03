"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #key: old node, value: new node
        mapping = {None:None}
        h1 = head
        while h1:
            mapping[h1]= Node(h1.val)
            h1 = h1.next

        h1 = head
        while h1:
            mapping[h1].next = mapping[h1.next]
            mapping[h1].random = mapping[h1.random]
            h1 = h1.next
        
        return mapping[head]

        

        

        
        