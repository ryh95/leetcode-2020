import math
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        l = int(math.log10((2 ** 31) - 1)) + 1
        # fulfill the 1st requirement
        for i in range(1,l):
            for j in range(i+1,i+l+1):
                can_match,res = self.match_fib_s(S,i,j)
                # fulfill the 2nd requirement
                if can_match and len(res) > 2: return res
        return []

    def match_fib_s(self,S,i,j):
        # fulfill the last requirement, ie. not start with 0
        if (len(S[:i]) > 1 and S[:i][0] == '0') or (len(S[i:j]) > 1 and S[i:j][0] == '0'): return False,[]
        if not S[:i] or not S[i:j]: return False,[]
        f1,f2 = int(S[:i]),int(S[i:j])
        k,res = j,[f1,f2]
        while k < len(S):
            f3 = f1 + f2
            # fulfill the 1st requirement
            if f3 > (2 ** 31) - 1: return False,[]
            f3_str = str(f3)
            if S[k:k+len(f3_str)] != f3_str:
                break
            k += len(f3_str)
            f1 = f2
            f2 = f3
            res.append(f3)
        if k < len(S): return False,[]
        return True,res

# test = "123456579"
test = '11235813'
test = '0123'
test = '1101111'
test = '1'
print(Solution().splitIntoFibonacci(test))