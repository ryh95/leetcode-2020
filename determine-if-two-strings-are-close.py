from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        c1 = Counter(word1)
        c2 = Counter(word2)
        if set(c1.values()) == set(c2.values()) and set(c1.keys()) == set(c2.keys()):
            return True
        return False

word1 = "abc"
word2 = "bca"
word1 = "a"
word2 = "aa"
word1 = "cabbba"
word2 = "abbccc"
word1 = "cabbba"
word2 = "aabbss"
print(Solution().closeStrings(word1,word2))