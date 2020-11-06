# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.cum_sum = 0
        self.helper(root)
        return root

    def helper(self,root):
        if root:
            self.helper(root.right)
            root.val += self.cum_sum
            self.cum_sum = root.val
            self.helper(root.left)

test = [5,None,13]
root = generate_tree(test)
re_root = Solution().convertBST(root)
print(re_root)