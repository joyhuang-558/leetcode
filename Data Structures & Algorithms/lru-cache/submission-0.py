class Node:
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):

        node.prev.next = node.next
        node.next.prev = node.prev
    

    def addLast(self,node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.addLast(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:
    # 情况一：key 已经存在
    # 1. 从 cache 中找到 node
    # 2. 更新 node.val
    # 3. remove(node)
    # 4. addLast(node)
    # 5. return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.addLast(node)
            return

        # 情况二：key 不存在
        # 1. 创建新 Node
        # 2. 存入 cache
        # 3. addLast(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.addLast(node)

        # 如果添加后超过容量
        # 1. 最久没用的节点是 self.head.next
        # 2. 从链表删除它
        # 3. 根据它的 key，从 cache 删除
        
        if len(self.cache)>self.cap:
            longest = self.head.next
            self.remove(longest)
            del self.cache[longest.key]

            
