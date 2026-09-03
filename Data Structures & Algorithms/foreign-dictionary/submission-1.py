

'''
我的思路就是，首先遍历所有的letter，然后搞一个dic。每个letter是key，value是【】。然后算一个max length = n。然后for i in range n开始遍历。
第一位，找出顺序。后面的append到前面的list里面，直到最后一位。
然后一直搞到最长的那个单词最后一位结束

然后就有了这个dic，key是letter，value是可以排在后面的。

这个dic：
node A：可以去node 啥


我需要，知道，每个node之前有几个node可以去，这个就是indegree。知道每个node之前有多少个node。

然后一个heap。每次弹出来indegree最小的。遍历他的nei，就是可以去什么。加入q。每次弹出nei这次最小的。

不存在的情况，就是，q完了，但是不等于len dic


'''

import heapq
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        indegree = {node: 0 for node in adj}
        print(indegree)

        visited = {node: False for node in adj}


        for node in adj:
            for nei in adj[node]:
                indegree[nei]+=1
        
        h = []
        for node, d in indegree.items():
            if d==0:
                heapq.heappush(h,[0,node])
                visited[node] = True
        
        res = []
        while h:
            degree,node = heapq.heappop(h)
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heapq.heappush(h, [0, nei])

        
        join_res = "".join(res)
        return "" if len(res)!=len(indegree) else join_res

#         "hrn","hrf","er","enn","rfnn"
#         h: e,r
#         e: r
#         r:n
#         n:f
#         f: 
#         indegree：
#         h：0
#         e: 1
#         r:2
#         n:1
#         f:1

# h e r n f 
        
#         a:a






    
        