

'''
想法：构造一个dic，key是letter，value是一个set，就是在这个之后可以放什么

这个dic的构造，遍历words，i和i+1拿出来，然后取短的word length这个来for 循环。如果碰到俩字母不一样的，append后的那个到前面的这个的set里面

dic构造完了之后，题目要求，return回来从小到大，那么就是一个topo问题。topo问题要有indegree。

遍历dic，算出来每个letter的indegree，就是多少在这个之前。这里因为是node所以需要用dic来存。

dic：node，value是number。

然后create一个q，加进去，indegree是0的node，说明这些node不需要谁 就可以访问，说明最小。
然后pop出去，加入到res里面。
同时遍历这个cur node 的nei，说明after 这个node访问了，哪些新的node可以被访问，同时对于这些新的node，indegree这个表也要更新，对应number要-1.然后如果碰到哪一个indegree 是0的继续append进来q。until q空了

最后返回，如果res长度不等于dic长度，就false。不然返回res


'''

import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create adj
        adj = defaultdict(set)
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1),len(word2))
            for j in range(min_len):
                if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                    return ""
                if word1[j]!=word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        #这里还需要一个，set node
        set_node = set()
        for word in words:
            for c in word:
                set_node.add(c)



        indegree = {node:0 for node in set_node}
        for node in adj:
            for nei in adj[node]:
                indegree[nei]+=1
        
        q = deque()
        for node in indegree:
            if indegree[node]==0:
                q.append(node)

        res = []
        while q:
            cur_node = q.popleft()
            res.append(cur_node)

            for nei in adj[cur_node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        print(res)
        return ''.join(res) if len(res)==len(indegree) else ""

        



    
            
                


        
        
      