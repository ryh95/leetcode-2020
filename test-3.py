from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res,sum_sub,max_sub,i = 0,0,0,0
        sub_digit = ''
        s = s + ' '
        cost.append(0)
        while i<len(s):
            if not sub_digit:
                sub_digit = s[i]
                sum_sub += cost[i]
                if max_sub < cost[i]: max_sub = cost[i]
                i += 1
                continue
            if s[i] == sub_digit:
                sum_sub += cost[i]
                if max_sub < cost[i]: max_sub = cost[i]
            else:
                sub_digit = s[i]
                res += sum_sub - max_sub
                sum_sub, max_sub = cost[i], cost[i]
            i += 1
        return res

s = "abaac"
cost = [1,2,3,4,5]
s = 'abc'
cost = [1,2,3]
s = "aabaa"
cost = [1,2,3,4,1]
s = 'a'
cost = [1]
print(Solution().minCost(s,cost))