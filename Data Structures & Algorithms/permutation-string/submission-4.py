class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        
            #写一个函数专门判断
        def freq_dic(s):
            d = {}
            for c in s:
                d[c] = d.get(c,0)+1
            return d
                

        d_target = freq_dic(s1)
        
        for i in range(len(s2)):
            l = i
            r = i+len(s1)

            if r>len(s2):
                return False
            cur_d = freq_dic(s2[l:r])
            if cur_d == d_target:
                return True
        return False
            
