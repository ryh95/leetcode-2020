import bisect
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # todo: make this code pass the test
        self.intervals = [(i,i+n) for i,n in enumerate(nums)]
        self.intervals_e = sorted(self.intervals,key=lambda x: x[1])
        self.intervals_s = sorted(self.intervals,key=lambda x: x[0])
        boundaries_e = [e[1] for e in self.intervals_e]
        boundaries_s = [e[0] for e in self.intervals_s]
        q, next_pos, res = [self.intervals[-1]],self.intervals[-1][0], 0
        while q and next_pos != 0:
            cur_interval = q.pop(0)
            next_interval = self.get_earliest_intersection(cur_interval, boundaries_e, boundaries_s)
            if next_interval:
                next_pos = next_interval[0]
                if next_pos == cur_interval[0]: break
                q.append(next_interval)
                res += 1
        return res


    def get_earliest_intersection(self, interval, boundaries_e, boundaries_s):
        i = bisect.bisect_left(boundaries_e,interval[0])
        set_e = set(self.intervals_e[i:])
        j = bisect.bisect_right(boundaries_s,interval[1])
        set_s = set(self.intervals_s[:j])
        intersect_set = set_s & set_e
        if intersect_set: return min(intersect_set,key=lambda x: x[0])

test = [2,3,1,1,4]
# test = [3,2,1,0,4]
print(Solution().jump(test))