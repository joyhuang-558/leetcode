class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def insert(self, word: str) -> None:
        #这里需要让node往下走
        node = self
        for i,c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = PrefixTree()
                node = node.children[c]
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self
        #i is index, c is letter (not node)
        for i,c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_end

        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i,c in enumerate(prefix):
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
        
        