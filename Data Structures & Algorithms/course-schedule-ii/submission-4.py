class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        ajd = {i:[] for i in range(numCourses)}

        for sec,fir in prerequisites:
            indegree[sec]+=1
            ajd[fir].append(sec)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in ajd[cur]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(res)==numCourses:
            return res
        return []
        