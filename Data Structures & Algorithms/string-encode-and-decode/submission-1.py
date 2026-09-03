
from collections import deque

class Solution:

    def encode(self, strs: List[str]) -> str:
        self.q = deque()
        for s in strs:
            len_s = len(s)
            for i,c in enumerate(s):
                if i == len_s-1:
                    self.q.append([c,True])
                else:
                    self.q.append([c,False])
        encode_res = ''.join([i[0]for i in self.q])
        print(encode_res)
        return encode_res




    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return [""]
        decode_res = []


        res = []
        while self.q:
            cur = self.q.popleft()
            res.append(cur[0])
            if cur[1]==True:
                cur_word = ''.join(res)
                decode_res.append(cur_word)
                res = []
        return decode_res

