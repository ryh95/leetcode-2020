class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t,t2s = {},{}
        for c_s,c_t in zip(s,t):
            if c_s not in s2t and c_t not in t2s:
                s2t[c_s] = c_t
                t2s[c_t] = c_s
            else:
                if c_s not in s2t or s2t[c_s] != c_t: return False
        return True

s = "egg"
t = "add"

# s = "foo"
# t = "bar"

# s = "paper"
# t = "title"

# s = ''
# t = ''

# s = "ab"
# t = "aa"
print(Solution().isIsomorphic(s,t))