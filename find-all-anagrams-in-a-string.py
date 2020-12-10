from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        return [i for i in range(len(s)-len(p)) if Counter(s[i:i+len(p)]) == cp]