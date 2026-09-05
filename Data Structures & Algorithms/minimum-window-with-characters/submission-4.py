class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dic = {}
        for c in t:
            target_dic[c] = target_dic.get(c,0)+1
        l=r=0
        res_l = 0
        res_r = 0
        
        cur_dic = {}
        
        def match(target_dic,cur_dic):
            for k,v in target_dic.items():
                if k in cur_dic and cur_dic[k]>=v:
                    continue
                else:
                    return False
            return True

        min_length = float('inf')
        
        for r in range(len(s)):
            cur_dic[s[r]] = cur_dic.get(s[r],0)+1
            #判断现在的窗口是否满足target dic
            
            while match(target_dic,cur_dic):
                if r-l+1<min_length:
                    min_length = r-l+1
                    res_l = l
                    res_r = r
                cur_dic[s[l]]-=1
                l+=1
        
        
        if min_length == float('inf'):
            return ""
        else:
            return s[res_l:res_r+1]
                





        


        