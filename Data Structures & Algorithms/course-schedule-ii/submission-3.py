class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        dic = {}
        q = deque()
        degree = [0]*numCourses
        for sec,fir in prerequisites:
            degree[sec]+=1
            if fir not in dic:
                dic[fir]=[]
            dic[fir].append(sec)
        for c,num in enumerate(degree):
            if num==0:
                q.append(c)
        while q:
            cur = q.popleft()
            res.append(cur)
            if cur not in dic:
                continue
            for nei in dic[cur]:
                degree[nei]-=1
                if degree[nei]==0:
                    q.append(nei)
        return res if len(res)== numCourses else []

        