# Definition for a binary tree node.
from collections import Counter
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.cout = Counter()
        self.helper(root)
        t = self.cout.most_common(1)[0][1]
        return [k for k,v in self.cout.items() if v == t]

    def helper(self, root):
        if root:
            self.cout[root.val] += 1
            self.helper(root.left)
            self.helper(root.right)