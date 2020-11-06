# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res_0 = self.helper(root,0)
        res_1_1 = self.helper(root,1,1)
        res_1_0 = self.helper(root,1,0)
        return max(res_0,res_1_1,res_1_0)


    def helper(self,root,conclude_root,start_from_root=1):
        if not root: return float('-inf')
        if hasattr(root,'res_0') and not conclude_root:
            return root.res_0
        if hasattr(root,'res_1_1') and conclude_root and start_from_root:
            return root.res_1_1
        if hasattr(root,'res_1_0') and conclude_root and not start_from_root:
            return root.res_1_0

        if not conclude_root:

            # left results
            left_res = max(
                self.helper(root.left, 0),
                self.helper(root.left, 1, 1),
                self.helper(root.left, 1, 0)
            )
            # right results
            right_res = max(
                self.helper(root.right, 0),
                self.helper(root.right, 1, 1),
                self.helper(root.right, 1, 0)
            )

            root.res_0 = max(left_res,right_res)
            return root.res_0

        else:

            # left results
            left_res = max(self.helper(root.left, 1, 1), 0)
            # right results
            right_res = max(self.helper(root.right, 1, 1), 0)

            if start_from_root:
                root.res_1_1 = max(left_res,right_res) + root.val
                return root.res_1_1
            else:
                root.res_1_0 = left_res + root.val + right_res
                return root.res_1_0


test = [5,4,8,11,None,13,4,7,2,None,None,None,1]
test = [-2]
test = [-2,-1]
root = generate_tree(test)

print(Solution().maxPathSum(root))