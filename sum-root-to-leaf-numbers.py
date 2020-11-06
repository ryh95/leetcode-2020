# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        self.numbers,self.vals = [],[]
        self.pre_order(root)
        return sum(self.vals)

    def pre_order(self,root):
        if root:
            self.numbers.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
            self.__save_number(root)
            self.numbers.pop()

    def __save_number(self,root):
        if not root.left and not root.right:
            self.vals.append(sum([n * (10 ** p) for n,p in zip(self.numbers,range(len(self.numbers))[::-1])]))

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

print(Solution().sumNumbers(a))

