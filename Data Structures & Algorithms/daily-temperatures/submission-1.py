class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        q = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while q and temperatures[i]>q[-1][0]:
                cur_value,cur_index = q.pop()
            
                res[cur_index]=i-cur_index
            
            q.append([temperatures[i],i])
        return res
                

        