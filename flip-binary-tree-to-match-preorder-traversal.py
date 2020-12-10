# Definition for a binary tree node.
from typing import List

from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:

        self.count_child(root,'left')
        self.count_child(root,'right')

        self.c = 0
        self.voyage,self.res = voyage,[]

        ret = self.helper(root)
        if ret: return [-1]

        return self.res

    def count_child(self, root, branch):
        if not root: return 0
        if hasattr(root,'n_left') and branch == 'left': return root.n_left
        if hasattr(root,'n_right') and branch == 'right': return root.n_right
        if branch == 'left':
            root.n_left = self.count_child(root.left,'left') + self.count_child(root.left,'right')
            if root.left: root.n_left += 1
            return root.n_left
        else:
            root.n_right = self.count_child(root.right,'left') + self.count_child(root.right,'right')
            if root.right: root.n_right += 1
            return root.n_right

    def helper(self,root):
        if root:
            if root.val != self.voyage[self.c]:
                return -1
            if root.left and root.right:
                ori_val = (root.left.val, root.right.val)
                left_id = self.c + 1
                right_id = self.c + root.n_left + 1
                voyage_val = (self.voyage[left_id], self.voyage[right_id])
                if ori_val == voyage_val:  # no need to flip
                    pass
                else:
                   right_id = self.c + root.n_right + 1
                   voyage_val = (self.voyage[right_id], self.voyage[left_id])
                   if ori_val == voyage_val: # need to flip
                       self.res.append(root.val)
                       root.left, root.right = root.right, root.left

            self.c += 1
            ret = self.helper(root.left)
            if ret: return ret
            ret = self.helper(root.right)
            if ret: return ret


# root = [1,2,3]
# voyage = [1,3,2]
# root = [1,2]
# voyage = [2,1]
# root = [1,2,3]
# voyage = [1,2,3]
# root = [1]
# voyage = [2]
# root = [1,2,3,None,None,4,5]
# voyage = [1,3,5,4,2]
# root = [1,None,2,None,3]
# voyage = [1,3,2]
# root = [2,1,4,5,None,3]
# voyage = [2,4,3,1,5]
root = generate_tree(root)
print(Solution().flipMatchVoyage(root,voyage))