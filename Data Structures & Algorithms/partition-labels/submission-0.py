class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        position = {}
        for i,item in enumerate(s):
            position[item]=i
        start=0
        end = 0
        output = []
        for i,item in enumerate(s):
            end = max(end,position[item])
            if i==end:
                output.append(end-start+1)
                start=i+1
        return output

            


        
        