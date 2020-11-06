# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover2(self, root: TreeNode) -> int:
        if not root: return 0
        if hasattr(self, 'ans'): return root.ans
        l_ch,r_ch = root.left,root.right
        option1,option2,option3 = 0,0,0

        if l_ch: option1 += self.minCameraCover2(root.left.left) + self.minCameraCover2(root.left.right)
        if r_ch: option1 += self.minCameraCover2(root.right.left) + self.minCameraCover2(root.right.right)

        if l_ch and l_ch.left: option2 += self.minCameraCover2(root.left.left.left) + self.minCameraCover2(
            root.left.left.right)
        if l_ch and l_ch.right: option2 += self.minCameraCover2(root.left.right.left) + self.minCameraCover2(
            root.left.right.right)
        if r_ch: option2 += self.minCameraCover2(root.right)

        if r_ch and r_ch.left: option3 += self.minCameraCover2(root.right.left.left) + self.minCameraCover2(
            root.right.left.right)
        if r_ch and r_ch.right: option3 += self.minCameraCover2(root.right.right.left) + self.minCameraCover2(
            root.right.right.right)
        if l_ch: option3 += self.minCameraCover2(root.left)

        root.ans = min(option1,option2,option3) + 1

        return root.ans

    def minCameraCover(self, root: TreeNode) -> int:
        res1 = self.helper(root, True)
        res2 = self.helper(root, False)
        # return res2
        return min(res1,res2)

    def helper(self, root: TreeNode, contains_root: bool) -> int:
        if not root and contains_root: return float('inf')
        if not root and not contains_root: return 0
        if contains_root and hasattr(root,'ans1'): return root.ans1
        if not contains_root and hasattr(root,'ans0'): return root.ans0
        if contains_root:
            # a = min(self.helper(root.left, True), self.helper(root.left, False))
            # b = min(self.helper(root.right, True), self.helper(root.right, False))
            # c = 1
            # root.ans1 = a + b + c

            l_ch_op1 = min(self.helper(root.left, True), self.helper(root.left, False))
            l_ch_res = l_ch_op1
            if root.left:
                l_ch_op2 = min(self.helper(root.left.left,True),self.helper(root.left.left,False)) \
                           + min(self.helper(root.left.right,True),self.helper(root.left.right,False))
                l_ch_res = min(l_ch_op1,l_ch_op2)
            r_ch_op1 = min(self.helper(root.right, True), self.helper(root.right, False))
            r_ch_res = r_ch_op1
            if root.right:
                r_ch_op2 = min(self.helper(root.right.left, True), self.helper(root.right.left, False)) \
                           + min(self.helper(root.right.right, True), self.helper(root.right.right, False))
                r_ch_res = min(r_ch_op1, r_ch_op2)
            root.ans1 = l_ch_res + r_ch_res + 1

            return root.ans1
        else:
            op1 = self.helper(root.left,True) + self.helper(root.right,False)
            op2 = self.helper(root.left,False) + self.helper(root.right,True)
            op3 = self.helper(root.left,True) + self.helper(root.right,True)
            root.ans0 = min(op1,op2,op3)
            return root.ans0

# test = [0,0,None,0,None,0,None,None,0]
# test = [0,0,0]
# test = [0,None,0,None,0,None,0,None,0,0,0,None,None,0,0]
# test = [0,None,0,0,0,None,None,0,0]
test = [None]
root = generate_tree(test)
print(Solution().minCameraCover(root))