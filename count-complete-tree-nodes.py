# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # todo: add a better solution

    def countNodes(self, root: TreeNode) -> int:
        self.c = 0
        self.helper(root)
        return self.c

    def helper(self,root):
        if root:
            self.c += 1
            self.helper(root.left)
            self.helper(root.right)
