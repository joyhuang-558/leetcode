
'''
思路，遍历board，做dfs
dfs这个函数，目的是，1. 在board上走上下左右四个方向。2. 在trie里面看是否有这个word/是否匹配/是否end。3. 需要visited这个来回溯

首先要构造出来一个trie，把words都放进去
比如：
    words = ["bat","cat","back","backend","stack"]
    这个就是从root开始，for word in words，然后for c in word，看c是否在node的children里面，这个c是letter，所以是看key，也就是直接.children。
    然后如果不在就加进去，然后node往下一个。
    就这样遍历完所有的node。

    首先要定义一个trie类，就是.children是一个{}，key是letter，value是这个类别

dfs((r,c),node),这个node是trie里面的。rc是board里面的位置。
然后遍历(r,c)上下左右合法的每个位置，然后看这个是否在node的children里面。如果在就继续dfs下去。

'''



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None
    def construct_trie(self,words):
    
        for word in words:
            #每次都需要从头插入
            node = self
            for c in word:
                if c in node.children:

                    node = node.children[c]
                else:
                    node.children[c] = TrieNode()
                    node = node.children[c]
               
            node.is_end = True
            node.word = word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        root.construct_trie(words)

        ds = [[1,0],[0,1],[-1,0],[0,-1]]

        total_r = len(board)
        total_c = len(board[0])

        res = []
        visited = [[0] * total_c for _ in range(total_r)]
        
        def dfs(r,c,node):
            visited[r][c]=1

            if node.word != None:
                res.append(node.word)
                node.word = None
            for dr,dc in ds:
                new_r = r+dr
                new_c = c+dc
                if (new_r in range(total_r) and new_c in range(total_c) and visited[new_r][new_c]==0):
                    cur_value = board[new_r][new_c]
                    if cur_value in node.children:
                        dfs(new_r,new_c,node.children[cur_value])
                else:
                    continue

            visited[r][c] = 0 

        for r in range(total_r):
            for c in range(total_c):
                if board[r][c] in root.children:
                    dfs(r,c,root.children[board[r][c]])
            
            
        



        return res



                    

        