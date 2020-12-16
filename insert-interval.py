import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        start_points,end_points = [i[0] for i in intervals],[i[1] for i in intervals]
        new_left,new_right = newInterval[0],newInterval[1]
        pos = bisect.bisect_right(start_points,new_left) - 1
        pos_right,pos_left = intervals[pos][1], intervals[pos][0]
        if pos < 0 or pos_right < new_left:
            left_bound = new_left
            i = pos + 1
        else:
            left_bound = pos_left
            i = pos
        pos = bisect.bisect_left(end_points,new_right)

        if pos > len(intervals)-1 or new_right < intervals[pos][0]:
            right_bound = new_right
            j = pos
        else:
            pos_right = intervals[pos][1]
            right_bound = pos_right
            j = pos + 1

        return intervals[:i] + [[left_bound,right_bound]] + intervals[j:]

intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = []
newInterval = [5,7]

intervals = [[1,5]]
newInterval = [2,7]
print(Solution().insert(intervals,newInterval))

