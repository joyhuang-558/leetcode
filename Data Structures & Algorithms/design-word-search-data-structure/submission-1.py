class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(index,node):
            if index == len(word):
                return node.is_end

            c = word[index]
            if c == ".":
                #这里要拿到node，不是abc这样的value。而dic里面，key是abc这样的，value才是node
                for child in node.children.values():
                    res = dfs(index+1,child)
                    if res:
                        return True
                return False
            else:
                if c in node.children:
                    return dfs(index+1,node.children[c])
                else:
                    return False
        return dfs(0,self)
                
                


