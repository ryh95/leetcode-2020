from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        fi,LEPS,LENS,=0,0,0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 0:
                fi = LENS + 1
                LEPS = fi
            elif nums[i] - nums[i-1] < 0:
                fi = LEPS + 1
                LENS = fi
        return fi + 1

test = [1]
test = [1,17,5,10,13,15,10,5,16,8]
test = [1,7,4,9,2,5]
test = [1,2,3,4,5,6,7,8,9]
print(Solution().wiggleMaxLength(test))