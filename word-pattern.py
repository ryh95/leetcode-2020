class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()): return False
        p2w,w2p = {},{}
        for p,w in zip(pattern,s.split()):
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p
            else:
                if p not in p2w or p2w[p] != w:
                    return False
        return True

# pattern = "abba"
# s = "dog cat cat dog"
# True
# pattern = "abba"
# s = "dog cat cat fish"
# False
# pattern = "aaaa"
# s = "dog cat cat dog"
# False
# pattern = "abba"
# s = "dog dog dog dog"
# False
print(Solution().wordPattern(pattern,s))