from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res,self.ress = [],[]
        self.k = k
        self.cands = list(range(1,10))
        self.helper(0,n,0)
        return self.ress

    def helper(self,j,target,n_calls):
        # if n_calls > self.k: return
        if target == 0 and n_calls == self.k:
            self.ress.append(self.res[:])
            return
        for i in range(j,9):
            if target - self.cands[i] < 0: break
            self.res.append(self.cands[i])
            if n_calls < self.k: self.helper(i+1,target-self.cands[i],n_calls+1)
            self.res.pop()

k,n = 3,7
# k,n = 3,9
# k,n = 1,9
print(Solution().combinationSum3(k,n))