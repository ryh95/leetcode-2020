from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        self.parents,redundancy,cluster = {},0,0
        for l in connections:
            if l[0] not in self.parents and l[1] not in self.parents:
                self.parents[l[1]] = l[0]
                self.parents[l[0]] = l[0]
                cluster += 1
                continue
            if l[0] not in self.parents and l[1] in self.parents:
                r_1 = self.find_root(l[1])
                self.join_trees(l[0],r_1)
                continue
            if l[1] not in self.parents and l[0] in self.parents:
                r_0 = self.find_root(l[0])
                self.join_trees(l[1], r_0)
                continue
            if l[0] in self.parents and l[1] in self.parents:
               r_0,r_1 = self.find_root(l[0]),self.find_root(l[1])
               if r_0 == r_1:
                   redundancy += 1
               else:
                   self.join_trees(r_0,r_1)
                   cluster -= 1

        n_remain_cluster = n - len(self.parents)
        if n_remain_cluster + cluster - 1 <= redundancy:
            return n_remain_cluster + cluster - 1
        else:
            return -1

    def find_root(self,node):
        while self.parents[node] != node:
            node = self.parents[node]
        return node

    def join_trees(self,a,b):
        self.parents[a] = b


# class Solution:
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         if len(connections) < n - 1:
#             return -1
#
#         fa = [x for x in range(n)]
#
#         def findset(x):
#             if x != fa[x]:
#                 fa[x] = findset(fa[x])
#             return fa[x]
#
#         part = n
#         for c0, c1 in connections:
#             p, q = findset(c0), findset(c1)
#             if p != q:
#                 part -= 1
#                 fa[p] = q
#
#         return part - 1


n = 4
connections = [[0,1],[0,2],[1,2]]
# n = 6
# connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# n = 6
# connections = [[0,1],[0,2],[0,3],[1,2]]
# n = 5
# connections = [[0,1],[0,2],[3,4],[2,3]]
print(Solution().makeConnected(n,connections))