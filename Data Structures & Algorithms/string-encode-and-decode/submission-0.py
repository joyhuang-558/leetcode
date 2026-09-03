class Solution:

    def encode(self, strs: List[str]) -> str:

# when no strs
        if not strs:
            return ""

        sizes = []
        res = ""

        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res
        # res = '4,4,4,3,#neetcodeloveyou'


    def decode(self, res: str) -> List[str]:
        if not res:
            return []
        
        sizes = []
        i = 0
        # res = '4,4,4,3,#neetcodeloveyou'
        while res[i] != '#':
            #get current num, because there may be 12, 13, so use inner while
            cur = ''
            while res[i] != ',':
                cur += res[i]
                i += 1
            # remember to change string to int for size  
            sizes.append(int(cur))
            i += 1
        # jump off #
        i += 1

        res1 = []
        for sz in sizes:
            res1.append(res[i:i+sz])
            i += sz
        return res1
            





