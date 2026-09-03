class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        far = 0
        cur_end = 0
        jump = 0
        for i,num in enumerate(nums):
            
            print(f"i = {i}, num = {num}")
            far = max(far,num+i)
            print(f"far = {far}, cur_end = {cur_end}")
            if far >= len(nums)-1:
                return jump+1
            

            
            if i == cur_end:
                print('i==cur_end')
                cur_end = far
                print(f"cur_end更新={far}")
                jump+=1
            


            
            
        