from collections import Counter


class Solution:
    def combinationSum(self,candidates,target):
        self.res,self.ress,self.candidates = [],[],set(candidates)
        self.n = len(self.candidates)
        self.c = Counter(candidates)
        self.candidates = sorted(self.candidates)
        self.helper(0,target)
        return self.ress

    def helper(self,j,target):
        if target == 0:
            self.ress.append(self.res[:])
            return
        for i in range(j,self.n):
            if target - self.candidates[i] < 0: break
            self.res.append(self.candidates[i])
            self.c[self.candidates[i]] -= 1
            if self.c[self.candidates[i]] == 0:
                self.helper(i+1,target-self.candidates[i])
            else:
                self.helper(i, target - self.candidates[i])
            self.res.pop()
            self.c[self.candidates[i]] += 1

candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [2,5,2,1,2]
target = 5
candidates = [1]
target = 1
print(Solution().combinationSum(candidates,target))