from functools import reduce
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        # special case
        if len(nums) < 2: return 0

        # radix sort base 10
        i,d = 0,max(len(str(e)) for e in nums)
        sorted_elements = [[n,n] for n in nums]
        while i < d:
            # generate keys(last digit)
            keys = []
            for e in sorted_elements:
                keys.append(e[1] % 10)
                e[1] //= 10
            # sort according to the keys
            sorted_elements = self.count_sort(sorted_elements,keys,10)
            i += 1

        return max(sorted_elements[i+1][0] - sorted_elements[i][0] for i in range(len(nums)-1))

    def count_sort(self, elements, keys, k):

        # elements: [(element,truncated_element),()]
        # keys: [key], used to sort the element
        # k: maximum of key
        #

        L = [[] for _ in range(k)]
        # stable count sort
        for e,key in zip(elements,keys):
            L[key].append(e)
        return reduce(lambda x,y: x+y,L)

# test = [3,6,9,1]
test = [1,10000000]
print(Solution().maximumGap(test))