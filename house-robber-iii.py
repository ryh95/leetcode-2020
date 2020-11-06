# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if hasattr(root, 'res'):
            return root.res

        option1 = self.rob(root.left) + self.rob(root.right)
        option2_left, option2_right = 0, 0
        if root.left: option2_left = self.rob(root.left.left) + self.rob(root.left.right)
        if root.right: option2_right = self.rob(root.right.left) + self.rob(root.right.right)
        option2 = option2_left + option2_right

        root.res = max(
            option1, option2 + root.val
        )

        return root.res

test = [3,2,3,None,3,None,1]
# test = [3,4,5,1,3,None,1]
# test = [3]
root = generate_tree(test)
sol = Solution()
print(sol.rob(root))