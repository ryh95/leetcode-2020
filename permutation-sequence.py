import math
from itertools import accumulate


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        candidate_digits = list(range(1,n+1))
        factos = [1] + list(accumulate(candidate_digits[:-1],lambda x,y: x*y))
        res = []
        for f in reversed(factos):
            id = math.ceil(k / f) - 1
            res.append(candidate_digits[id])
            k = k % f
            del candidate_digits[id]
        return ''.join([str(i) for i in res])

    # def getPermutation(self, n: int, k: int) -> str:
    #     self.n,self.k,self.res,self.counter = n,k,[],0
    #     D = OrderedDict((i,None) for i in range(1,n+1))
    #     res = self.getKthPermutation(0,D)
    #     return ''.join([str(i) for i in res])

    # def getKthPermutation(self,i,D):
    #     for digit in D.keys():
    #         self.res.append(digit)
    #         D_ = copy.deepcopy(D)
    #         D_.pop(digit)
    #         res = self.getKthPermutation(i+1,D_)
    #         if res: return res
    #         self.res.pop()
    #     if i == self.n: self.counter += 1
    #     if self.counter == self.k: return self.res
    #     return None

n,k = 3,3
# n,k = 1,1
# n,k = 4,9
sol = Solution()
print(sol.getPermutation(n,k))