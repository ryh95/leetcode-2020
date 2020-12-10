class Solution:
    def countSubstrings(self, s: str) -> int:
        n,res = len(s),0
        f = [[False for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                f[i][i+l] = f[i+1][i+l-1] and s[i] == s[i+l] if i+1 <= i+l-1 else s[i] == s[i+l]
                if f[i][i+l]: res += 1
        return res

s = 'abc'
s = 'aaa'
print(Solution().countSubstrings(s))