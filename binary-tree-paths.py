# Definition for a binary tree node.
from typing import List

from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res,self.ress = [],[]
        self.in_order(root)
        return self.ress

    def in_order(self,root):
        if root:
            self.res.append(str(root.val))
            self.in_order(root.left)
            self.in_order(root.right)
            if root.left is None and root.right is None:
                self.ress.append('->'.join(self.res))
            self.res.pop()

test = [1,2,3,None,5]
test = [1]
test = []
root = generate_tree(test)
sol = Solution()
print(sol.binaryTreePaths(root))