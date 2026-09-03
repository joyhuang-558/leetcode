class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #这个dic代表，key指向val，上完key，val的课程的degree就可以-1
        dic = {}
        #这个degree是说，每一个course，需要的前置课程数量
        degree = [0]*numCourses
        for sec,fir in prerequisites:
            degree[sec]+=1
            if fir not in dic:
                dic[fir] = []
            dic[fir].append(sec)
        q = deque()
        for c, num in enumerate(degree):
            if num == 0:
                q.append(c)
        while q:
            cur = q.popleft()
            if cur not in dic:
                continue
            for nei in dic[cur]:
                degree[nei]-=1
                if degree[nei]==0:
                    q.append(nei)
        for i in degree:
            if i !=0:
                return False 
        return True
        





            

        
        