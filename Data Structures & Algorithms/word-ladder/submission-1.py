from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. 拿到word。2. 通过word拿到patterns，by using mapping function。3. 拿到patterns之后，通过dic拿到可以遍历所有的pattern，以及对应的wordlist，然后再遍历这些word list，把word加入q。q里面一直是word。如果这个word是endword就结束了。
        #需要一个visited，就是说如果这个visited过了就continue
        visited = set()
        visited.add(beginWord)
        if endWord not in set(wordList):
            return 0
        
        dic = defaultdict(list)
        # dic: pattern - word_list

        bg_list = self.mapping(beginWord)
        for pattern in bg_list:
            dic[pattern].append(beginWord)

        for word in wordList:
            map_list = self.mapping(word)
            for pattern in map_list:
                dic[pattern].append(word)
        res = 1
        q = deque()
        q.append(beginWord)
        # q里面是word
        while q:
            length = len(q)
            for i in range(length):
                cur_word = q.popleft()
                cur_patterns = self.mapping(cur_word)
                for pattern in cur_patterns:
                    word_list = dic[pattern]
                    for word in word_list:
                        if word in visited:
                            continue
                        elif word == endWord:
                            return res+1
                        else:
                            visited.add(word)
                            q.append(word)
            res+=1
        return 0
                        
        
        

    #这个函数，对于每一个传入的word，每一位都变成*，然后output是len（word）的一个list
    def mapping(self,word):
        map_list = []
        for i,c in enumerate(word):
            map_list.append(word[:i]+"*"+word[i+1:])
        return map_list
    

        