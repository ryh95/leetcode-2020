# Definition for singly-linked list.
from collections import deque
import sys
from utils import generate_linked_list2, generate_tree
sys.setrecursionlimit(1000000)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root: return False
        # if head.val != root.val:
        #     return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
        # else:
        #     return self.helper(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def helper(self, head, root):
        if not head: return True
        if not root or root.val != head.val: return False
        return self.helper(head.next,root.left) or self.helper(head.next,root.right)


    def isSubPath2(self, head: ListNode, root: TreeNode) -> bool:
        self.i, self.j = -1, -1
        self.path = self.get_path(head)
        self.stack, self.match_pos = deque(), []
        res = self.in_order(root)
        return res

    def in_order(self,node):
        if node:
            # insert
            self.stack.append(node.val)
            self.j += 1
            if self.stack[self.j] == self.path[self.i+1]:
                if self.j == 0:
                    self.match_pos.append(0)
                else:
                    self.match_pos.append(self.match_pos[self.j-1] + 1)
            elif self.stack[self.j] == self.path[self.i]:
                self.match_pos.append(self.match_pos[self.j-1])
            else:
                self.match_pos.append(-1)
            self.i = self.match_pos[self.j]
            if self.i == len(self.path) - 1: return True
            ans = self.in_order(node.left)
            if ans: return ans
            ans = self.in_order(node.right)
            if ans: return ans
            # pop
            # if self.i >= 0 and (self.stack[self.j] == self.path[self.i]):
            self.i = self.match_pos[self.j-1]
            self.stack.pop()
            self.match_pos.pop()
            self.j -= 1
        return False

    def get_path(self, head: ListNode):
        path = []
        while head:
           path.append(head.val)
           head = head.next
        return path

# array = [4,2,8]
# array = [3]
array = [1,10]

head = generate_linked_list2(array)
# tree = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
# tree = [1,5,3,None,4,None,3]
tree = [1,None,1,10,1,9]

root = generate_tree(tree)
sol = Solution()
res = sol.isSubPath(head,root)
print(res)
# print(sol.i)
