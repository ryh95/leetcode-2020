from collections import Counter
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda x: (bin(x).count("1"),x))

arr = [0,1,2,3,4,5,6,7,8]
arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(Solution().sortByBits(arr))
