from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict: return False
        L = {len(w) for w in wordDict}
        w = [False for _ in range(len(s))] + [True for _ in range(max(L)+1)]
        worddict = set(wordDict) | set([''])
        for i in range(len(s),-1,-1):
            w[i] = any([((s[i:i + l] in worddict) and w[i + l]) for l in L])
        return w[0]



s = ""
wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "applepenapple"
# wordDict = ["apple", "pen"]
# s = "leetcode"
# wordDict = ["leet", "code"]
# s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s,wordDict))