# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        traversal_nodes = []
        res = []
        if root is None: return []
        traversal_nodes.append([root])
        res.append([root.val])
        while traversal_nodes:
            level_nodes = []
            for node in traversal_nodes[0]:
                level_nodes += [n for n in [node.left,node.right] if n is not None]
            if level_nodes: 
                traversal_nodes.append(level_nodes)
                res.append([node.val for node in level_nodes])
            traversal_nodes.pop(0)
        return res

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(7)
f=TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(Solution().levelOrder(a)) 