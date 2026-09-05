class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dic = {}
        for c in t:
            target_dic[c] = target_dic.get(c,0)+1
        l=r=0
        res_l = 0
        res_r = 0
        
        cur_dic = {}
        have = 0
        need = len(target_dic)

        min_length = float('inf')
        
        for r in range(len(s)):
            cur_dic[s[r]] = cur_dic.get(s[r],0)+1
            #判断现在的窗口是否满足target dic
            if s[r] in target_dic and target_dic[s[r]]==cur_dic[s[r]]:
                have += 1
                while have == need:
                    if r-l+1<min_length:
                        min_length = r-l+1
                        res_l = l
                        res_r = r
                    cur_dic[s[l]]-=1
                    if s[l] in target_dic and cur_dic[s[l]]<target_dic[s[l]]:
                        have-=1
                    l+=1
        
        
        if min_length == float('inf'):
            return ""
        else:
            return s[res_l:res_r+1]
                





        


        