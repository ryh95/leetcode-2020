from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res,self.ress,self.candidates = [],[],candidates
        candidates.sort()
        self.helper(0,target)
        return self.ress

    def helper(self,j,target):
        if target == 0:
            self.ress.append(self.res[:])
            return
        for i in range(j,len(self.candidates)):
            if target - self.candidates[i] < 0: break
            self.res.append(self.candidates[i])
            self.helper(i,target-self.candidates[i])
            self.res.pop()

candidates = [2,3,5]
target = 8
candidates = [2,6,3,7]
target = 7
candidates = [4]
target = 5
print(Solution().combinationSum(candidates,target))