from collections import OrderedDict, defaultdict
from queue import Queue
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        traverse_queue = Queue()
        n_visit = OrderedDict((i, 0) for i in range(n))
        visited_lands,visited_waters = defaultdict(set),defaultdict(set)
        # n_visited_lands, n_visited_waters = 0, 0
        n_islands = 0
        while n_visit:
            i, j = next(iter(n_visit.items()))
            if j == m:
                n_visit.popitem(False)
                continue
            j_to_visit = {k for k in range(m)} - visited_lands[i] - visited_waters[i]
            traverse_queue.put((i, next(iter(j_to_visit))))
            new_island = 0
            while not traverse_queue.empty():
                i, j = traverse_queue.get()
                if grid[i][j] == '1' and (j not in visited_lands[i]):
                    new_island = 1
                    visited_lands[i].add(j)
                    n_visit[i] += 1
                    # n_visited_lands += 1
                    # 上下左右四个方向走
                    if j < m-1: traverse_queue.put((i, j + 1)) # 右走
                    if i < n-1: traverse_queue.put((i + 1, j)) # 下走
                    if j > 0: traverse_queue.put((i,j-1)) # 左走
                    if i > 0: traverse_queue.put((i-1,j)) # 上走
                elif grid[i][j] == '0' and (j not in visited_waters[i]):
                    # n_visited_waters += 1
                    visited_waters[i].add(j)
                    n_visit[i] += 1
            n_islands += new_island
        return n_islands

# test_grid = [
#     ['1','1','0','0','0'],
#     ['1','1','0','0','0'],
#     ['0','0','1','0','0'],
#     ['0','0','0','1','1'],
# ]
# test_grid = [
#     ['1','1','1','1','0'],
#     ['1','1','0','1','0'],
#     ['1','1','0','0','1'],
#     ['0','0','1','1','0'],
# ]
# test_grid = [
#     ['1','1','1'],
#     ['0','1','0'],
#     ['1','1','1']
# ]
# test_grid = [
#     ['1','1','1','0','1'],
# ]
# test_grid = [
#     ['1'],
#     ['1'],
#     ['1'],
#     ['1'],
#     ['1']
# ]
# test_grid = [[]]
# test_grid = [
#     ['1','1','1','1','0'],
#     ['1','1','0','0','1'],
#     ['1','1','0','0','0'],
#     ['1','1','1','1','1'],
# ]
test_grid = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
 ]
n_islands = Solution().numIslands(test_grid)
print(n_islands)