from collections import defaultdict, deque
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = self.create_adjacency_list(equations,values)
        arrived_nodes = {}
        for n in g.keys():
            if n not in arrived_nodes:
                arrived_nodes[n] = (n,1)
                q = deque([n])
                while q:
                    cur_node = q.pop()
                    if cur_node not in g: continue
                    for neighbor,value in g[cur_node]:
                        if neighbor not in arrived_nodes:
                            q.append(neighbor)
                            arrived_nodes[neighbor] = (arrived_nodes[cur_node][0],arrived_nodes[cur_node][1]*value)
        res = []
        for s,e in queries:
            if s in arrived_nodes and e in arrived_nodes:
                if arrived_nodes[s][0] != arrived_nodes[e][0]:
                    res.append(-1.0)
                else:
                    res.append(arrived_nodes[e][1]/arrived_nodes[s][1])
            else:
               res.append(-1.0)
        return res

    def create_adjacency_list(self,equations,values):
        g = defaultdict(deque)
        for (s,e),v in zip(equations,values):
            g[s].append((e,v))
            g[e].append((s,1/v))
        return g

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# equations = [["a","b"],["b","c"],["bc","cd"]]
# values = [1.5,2.5,5.0]
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

equations = [["a","e"],["b","e"]]
values = [4.0,3.0]
queries = [["a","b"],["e","e"],["x","x"]]

print(Solution().calcEquation(equations,values,queries))