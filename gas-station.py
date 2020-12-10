from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # todo: finish and submit the code
        pass

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas  = [2,3,4]
cost = [3,4,3]

# gas = [3]
# cost = [4]
#
# gas = [5,8,2,8]
# cost = [6,5,6,6]

gas = [5,5,1,3,4]
cost = [8,1,7,1,1]

print(Solution().canCompleteCircuit(gas,cost))