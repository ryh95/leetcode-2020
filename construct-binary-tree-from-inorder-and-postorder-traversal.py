# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     self.in_num2id = {v:i for i,v in enumerate(inorder)}
    #     self.post_num2id = {v:i for i,v in enumerate(postorder)}
    #     self.n = len(postorder)
    #     root = self.helper(inorder,postorder,len(inorder))
    #     return root
    #
    # def helper(self,inorder,postorder,parent_pos) -> TreeNode:
    #     root_val = postorder[-1]
    #     root_node = TreeNode(root_val)
    #     inorder_root_pos = self.in_num2id[root_val] - parent_pos - 1 if self.in_num2id[root_val] > parent_pos else self.in_num2id[root_val]
    #     left_in,right_in = inorder[:inorder_root_pos],inorder[inorder_root_pos+1:]
    #     if not left_in and not right_in: return root_node
    #     if self.in_num2id[left_in[0]] > parent_pos:
    #         parent_left_size = self.n - len(inorder) - 1
    #         pos1 = self.post_num2id[left_in[0]] - parent_left_size
    #         pos2 = self.post_num2id[right_in[0]] - parent_left_size
    #     else:
    #         pos1 = self.post_num2id[left_in[0]]
    #         pos2 = self.post_num2id[right_in[0]]
    #     left_post = postorder[pos1:pos2]
    #     right_post = postorder[pos2:-1]
    #     root_node.left = self.helper(left_in,left_post,self.in_num2id[root_val])
    #     root_node.right = self.helper(right_in,right_post,self.in_num2id[root_val])
    #     return root_node
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        root = postorder[-1]
        root_node = TreeNode(root)
        inorder_root_pos = inorder.index(root)
        left_in, right_in = inorder[:inorder_root_pos], inorder[inorder_root_pos + 1:]
        if not left_in and not right_in: return root_node
        if not left_in:
            left_post, right_post = [], postorder[:-1]
        elif not right_in:
            left_post, right_post = postorder[:-1], []
        else:
            pos = postorder.index(inorder[inorder_root_pos + 1])
            left_post, right_post = postorder[:pos], postorder[pos:-1]
        root_node.left = self.buildTree(left_in,left_post)
        root_node.right = self.buildTree(right_in,right_post)
        return root_node

test_in,test_post = [14,9,6,3,15,20,7],[14,6,9,15,7,20,3]
# test_in,test_post = [2,1],[2,1]
# test_in = [2,3,1]
# test_post = [3,2,1]
# test_in = [1,2,3]
# test_post = [3,2,1]
test_in = [1,2,3,4]
test_post = [1,4,3,2]
root = Solution().buildTree(test_in,test_post)
print(root)
