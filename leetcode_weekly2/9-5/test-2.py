class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        if '1' not in set(s):
            return ((n-2)*(n-1)//2) % (10 ** 9 + 7)
        d = {'0':0,'1':0}
        for c in s:
            d[c] += 1
        if d['1'] % 3 != 0: return 0
        counter = 0
        thre = d['1'] // 3
        pos1,pos2,pos3,pos4 = 0,0,0,0
        f1,f2,f3,f4 = False,False,False,False
        for id,c in enumerate(s,1):
            if c == '1': counter += 1
            if not f1 and counter == thre:
                pos1 = id
                f1 = True
            if not f2 and counter > thre:
                pos2 = id
                f2 = True
            if not f3 and counter == 2*thre:
                pos3 = id
                f3 = True
            if not f4 and counter > 2*thre:
                pos4 = id
                f4 = True
        return (pos2-pos1)*(pos4-pos3) % (10 ** 9 + 7)

s = '100100010100110'
sol = Solution()
print(sol.numWays(s))