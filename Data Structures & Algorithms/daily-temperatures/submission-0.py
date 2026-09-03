class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        #put index in stack
        stack = []
        for i,temp in enumerate(temperatures):
            print(f"i:{i}  temp:{temp}")
            while stack and temp>temperatures[stack[-1]]:
                print(f"stack:{stack}  temp:{temp}")
                ans[stack[-1]] = i-stack[-1]
                print(f"ans:{ans}")
                stack.pop()
            stack.append(i)
        return ans



        