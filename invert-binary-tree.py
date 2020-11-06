# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return_root = root
        self.pre_order_invert(root)
        return return_root

    def pre_order_invert(self,root):
        if root:
            root.left,root.right = root.right,root.left
            self.pre_order_invert(root.left)
            self.pre_order_invert(root.right)

test = [4,2,7,1,3,6,9]
root = generate_tree(test)
return_root = Solution().invertTree(root)
print(return_root)