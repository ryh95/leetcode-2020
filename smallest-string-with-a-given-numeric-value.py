class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d = {i:c for i,c in enumerate('zabcdefghijklmnopqrstuvwxyz',0)}

        x = 0
        while (k - x) <= 26 * (n - x):
            x += 1

        x -= 1

        r = d[(k - x) % 26]

        res = x * 'a' + r + (n - x - 1) * 'z'

        return res

n = 5
k = 73
n = 3
k = 27
n = 9
k = 34
print(Solution().getSmallestString(n,k))