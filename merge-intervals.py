import bisect
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        sorted_intervals = sorted(intervals,key=lambda x: x[1])
        return self.merge_main(sorted_intervals,0,len(intervals))

    def merge_main(self,intervals,i,j):
        if len(intervals[i:j]) == 1: return [intervals[i]]
        m = i + (j-i) // 2
        left = self.merge_main(intervals,i,m)
        right = self.merge_main(intervals,m,j)
        merged_intervals = self.merge_two_interval_sets(left,right)
        return merged_intervals

    def merge_two_interval_sets(self,l,r):
        rl = r[0]
        pos = bisect.bisect_right([e[0] for e in l],rl[0]) - 1 # upper bound of less than or equal to
        if pos == -1:
            merged_intersection = [[rl[0], rl[1]]]
            if r[1:]: merged_intersection = merged_intersection + r[1:]
            return merged_intersection
        if rl[0] - l[pos][0] <= l[pos][1] - l[pos][0]:
            merged_intersection = [[l[pos][0],rl[1]]]
            if l[:pos]: merged_intersection = l[:pos] + merged_intersection
        else:
            merged_intersection = [[rl[0], rl[1]]]
            if l[:pos+1]: merged_intersection = l[:pos+1] + merged_intersection
        if r[1:]: merged_intersection = merged_intersection + r[1:]
        return merged_intersection

    def two_intervals_can_merge(self,i1,i2):
        if i1[1] < i2[0]: return False
        if i2[1] < i1[0]: return False
        return True

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,2]]
# intervals = [[1,4],[0,4]]
# intervals = [[2,3],[4,5],[6,7],[8,9],[1.5,10]]
# intervals = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
# intervals = [[3,3],[4,5],[4,6]]
# intervals = [[3,3],[3,5],[1,3],[2,4],[0,0],[4,6],[2,2],[1,2],[3,3],[4,4]]
print(Solution().merge(intervals))