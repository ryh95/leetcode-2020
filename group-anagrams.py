from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
           d[frozenset((k,v) for k,v in Counter(s).items())].append(s)
        return list(d.values())

test = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = []
print(Solution().groupAnagrams(test))