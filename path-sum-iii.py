# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.res += self.helper(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        return self.res

    def helper(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        res = self.helper(root.left, sum - root.val) + self.helper(root.right, sum - root.val)
        if root.val == sum: res += 1
        return res


test = [10,5,-3,3,2,None,11,3,-2,None,1]
test = [1,2,0,-2,-1]
root = generate_tree(test)
sol = Solution()
print(sol.pathSum(root,1))