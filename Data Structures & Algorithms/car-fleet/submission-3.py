class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 搞一个[pos,time],time = target-pos/speed
        s = []
        for i in range(len(position)):
            s.append([position[i],(target-position[i])/speed[i]])
        s.sort(reverse = False)
       

        num_fleet = 0
        while s:
            if num_fleet == 0:
              

                pre = s.pop()
                pre_time = pre[1]
                
                num_fleet+=1
               
            else:
                cur = s.pop()
               
                cur_time = cur[1]
                if cur_time>pre_time:
                    num_fleet+=1

                    pre_time = cur_time
            
                else:
                    pass

                   
            
        return num_fleet








        