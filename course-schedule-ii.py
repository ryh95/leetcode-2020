from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = self.get_adj_list(numCourses,prerequisites)
        self.visited,self.stack,self.marked_nodes = set(),[],set()
        self.has_cycle = False
        for v in g:
            if v not in self.visited:
                self.marked_nodes.add(v)
                self.visited.add(v)
                self.dfs_visit(v,g)
                # if self.has_cycle: return []
                self.marked_nodes.remove(v)
        self.stack.reverse()
        if self.has_cycle: return []
        # if len(set(self.stack)) < len(self.stack): return []
        return self.stack

    def dfs_visit(self,v,g):
        flag = False
        for u in g[v]:
            if u not in self.marked_nodes:
                self.marked_nodes.add(u)
            else:
                self.has_cycle = True
                flag = True
            if u not in self.visited:
                self.visited.add(u)
                self.dfs_visit(u,g)
            # if not self.has_cycle:
            if not flag:
                self.marked_nodes.remove(u)
        self.stack.append(v)

    def get_adj_list(self, numCourses, prerequisites):
        g = defaultdict(list)
        end_set,start_set = set(),set()
        for e,s in prerequisites:
            g[s].append(e)
            end_set.add(e)
            start_set.add(s)
        for v in end_set - start_set:
            g[v] = []
        for v in set(range(numCourses)) - set(g.keys()):
            g[v] = []
        return g

# test = [[1,0],[2,0],[3,1],[3,2]]
test = [[1,0],[2,1],[3,2],[0,3]]
# test = [[2,0],[1,0],[3,1],[3,2],[1,3]]
res = Solution().findOrder(4,test)
print(res)