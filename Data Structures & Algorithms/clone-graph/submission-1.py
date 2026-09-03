"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        dic = {}
        dic[node]=Node(node.val)
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in dic:
                    dic[nei] = Node(nei.val)
                    q.append(nei)
                dic[cur].neighbors.append(dic[nei])
        return dic[node]


        