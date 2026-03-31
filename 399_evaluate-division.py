"""
399. Evaluate Division

You are given an array of variable pairs equations and an array
 of real numbers values, where equations[i] = [Ai, Bi] and values[i] 
 represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] 
represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer 
cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the 
queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations 
are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Idea:
1) build a graph with nodes (a->b) and edge (weight: v), also b->a weight 1/v
2) for a given nodes (c,d), search the path in the graph from c to d
"""

from typing import DefaultDict, get_args
from collections import deque


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # build a graph with nodes and weight
        graph = DefaultDict(list)        
        N = len(equations)
        for i in range(N):
            a,b = equations[i][0], equations[i][1]            
            v = values[i]
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
        

        # find a path from node c to node d
        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1
            q = deque([(start, 1.0)])
            visited = set()
            while q:
                node, val = q.popleft()
                if node == end:
                    return val
                visited.add(node)
                for next, wt in graph[node]:
                    if next not in visited:
                        q.append((next, val*wt))
                    
            return -1.0


        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            q = deque([(start, 1.0)])
            visited = set()
            while q:
                node, val = q.popleft()
                if node == end:
                    return val
                visited.add(node)
                for nxt, w in graph[node]:
                    if nxt not in visited:
                        q.append((nxt, val * w))
            return -1.0



        # query each item in the queries
        return [bfs(c,d) for c, d in queries]


# main test
if __name__ == "__main__":
    #Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
    #queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    #Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    sol = Solution()
    print(sol.calcEquation(equations, values, queries))
                
        