from collections import defaultdict
from typing import List

class Node(object):

    def __init__(self,id,val):
        self.id = id
        self.val = val
        self.ids = set([id])
        self.left = None
        self.right = None


class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        has_number,id_dict,res = [0 for _ in range(101)],defaultdict(set),{}
        for id_t,t in enumerate(T):
            has_number[t] = 1
            id_dict[t].add(id_t)
            temps = [i + 30 for i,flag in enumerate(has_number[30:t]) if flag]
            for t in temps:
                for id in id_dict[t]:
                    # if id in res: continue
                    res[id] = id_t - id
                has_number[t] = 0
                id_dict[t] = set()
        return [res.get(i,0) for i in range(len(T))]

    ## a BST solution
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     if len(T) == 1: return [0]
    #     self.D={}
    #     root = Node(0,T[0])
    #     for i in range(1,len(T)):
    #         self.build_bst(root,Node(i,T[i]))
    #     return [self.D.get(i,0) for i in range(len(T))]
    #
    # def build_bst(self,root,node):
    #     if node.val > root.val:
    #         computed_nodes = set()
    #         for id in root.ids:
    #             if id in self.D:
    #                 computed_nodes.add(id)
    #                 continue
    #             self.D[id] = node.id - id
    #         root.ids -= computed_nodes
    #         if not root.right:
    #             root.right = node
    #             return
    #         self.build_bst(root.right,node)
    #     else:
    #         root.ids.add(node.id)
    #         if not root.left:
    #             root.left = node
    #             return
    #         self.build_bst(root.left,node)
    #     root.ids = set(id for id in root.ids if id not in self.D)

tests = [
    # [73, 74, 75, 71, 69, 72, 76, 73],
    # [73,74,75,71,69,59,72,76,73],
    # [74,75,76]
    # [55,38,53,81,61,93,97,32,43,78]
    [34,80,80,34,34,80,80,80,80,34]
]
for test in tests:
    print(Solution().dailyTemperatures(test))