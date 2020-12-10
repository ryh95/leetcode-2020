import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0 for _ in range(amount + 1)]
        for i in range(1,len(f)):
            f[i] = min(f[i - c] if i - c >= 0 else float('inf') for c in coins) + 1
        return -1 if math.isinf(f[-1]) else f[-1]

# coins = [1, 2, 5]
# amount = 11
coins = [2]
amount = 3
# coins = [1]
# amount = 0
# coins = [1]
# amount = 2
# coins = [1]
# amount = 1
print(Solution().coinChange(coins,amount))
