# Definition for a binary tree node.
from typing import List

from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

test = [1,None,2,3]
root = generate_tree(test)
print(Solution().inorderTraversal(root))