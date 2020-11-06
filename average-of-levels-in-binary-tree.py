# Definition for a binary tree node.
from functools import reduce
from typing import List

from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        q,res = [[root]],[root.val]
        while q:
            cur_level = q.pop(0)
            next_level = reduce(lambda x,y: x+y,([e.left,e.right] for e in cur_level if e))
            if any(next_level): q.append(next_level)
            next_level_val = [e.val for e in next_level if e]
            if next_level_val: res.append(sum(next_level_val)/len(next_level_val))
        return res

test = [3,9,20,None,None,15,7]
root = generate_tree(test)
print(Solution().averageOfLevels(root))