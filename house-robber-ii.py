from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # deal with special cases
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)

        fi1,ress1 = self.rob_(nums[1:])
        s,e = ress1[0]
        if s == 1 and e == n - 3:
            fi1 += nums[0]

        fi2, ress2 = self.rob_(nums[:-1])
        s,e = ress2[0]
        if s == 1 and e == n - 3:
            fi2 += nums[-1]

        return max(fi1,fi2)

    def rob_(self,nums: List[int]):
        n = len(nums)
        fi_2,ri_2 = nums[0], [[0,0]]
        if nums[0] < nums[1]:
            fi_1,ri_1 = nums[1], [[1,1]]
        elif nums[0] > nums[1]:
            fi_1, ri_1 = nums[0], [[0,0]]
        else:
            fi_1, ri_1 = nums[1], [[1,1]]
        i = 2
        if i == n: return fi_1,ri_1
        while i<n:
            if fi_1 < fi_2 + nums[i]:
                fi = fi_2 + nums[i]
                ri = [[res[0],i] for res in ri_2]
            elif fi_1 > fi_2 + nums[i]:
                fi = fi_1
                ri = ri_1
            else:
                fi = fi_1
                ri = ri_1 + [[res[0],i] for res in ri_2]
                # 减少ri中的结果，选start with 1的，如果没有start with 1的，随便选一个0的
                select_0 = True
                for res in ri:
                    if res[0] == 1:
                        ri = [res]
                        select_0 = False
                        break
                if select_0: ri = [ri[0]]
            fi_2,ri_2 = fi_1,ri_1
            fi_1,ri_1 = fi,ri
            i += 1
        return fi,ri

# test = [1,2,3,1,8,10,7]
test = [1,2,1,0]
# test = [0,0,0,0,0,0,0,0]
# test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(Solution().rob(test))