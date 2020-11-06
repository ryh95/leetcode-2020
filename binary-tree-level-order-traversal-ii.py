# Definition for a binary tree node.
from collections import deque
from functools import reduce
from typing import List

from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        dq,res = deque([[root]]),[]
        while dq:
            level = dq.popleft()
            res.append([e.val for e in level if e])
            next_level = reduce(lambda x,y: x+y,([e.left,e.right] for e in level if e))
            if any(next_level): dq.append(next_level)
        return res[::-1]

test = [3,9,20,None,None,15,7]
test = [3]
test = []
root = generate_tree(test)
print(Solution().levelOrderBottom(root))