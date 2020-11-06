# Definition for a binary tree node.
from utils import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.parent = {}
        self.parent[root] = None
        self.track_parent(root)
        p_parents,p_parent = [],p
        q_parents,q_parent = set(),q
        while p_parent is not None:
            p_parents.append(p_parent)
            p_parent = self.parent[p_parent]
        while q_parent is not None:
            q_parents.add(q_parent)
            q_parent = self.parent[q_parent]
        # check the lowestCommonAncestor
        for parent in p_parents:
            if parent in q_parents:
                return parent


    def track_parent(self, root):
        if root:
            if root.left: self.parent[root.left] = root
            if root.right: self.parent[root.right] = root
            self.track_parent(root.left)
            self.track_parent(root.right)

test = [3,5,1,6,2,0,8,None,None,7,4]
root = generate_tree(test)
sol = Solution()
res = sol.lowestCommonAncestor(root,5,1)
print(res.val)