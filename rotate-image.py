from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # todo: give a better solution
        if not matrix: return
        new_matrix = [[] for _ in range(len(matrix[0]))]
        for r in matrix:
            for c_id,e in enumerate(r):
                new_matrix[c_id].append(e)
        for i,r in enumerate(new_matrix):
            matrix[i] = r[::-1]

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
matrix = [[1]]
Solution().rotate(matrix)
print(matrix)