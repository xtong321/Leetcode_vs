"""
547. Number of Provinces

There are n cities. Some of them are connected, 
while some are not. If city a is connected directly 
with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected 
cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """        
        def dfs(i):
            visited[i] = True
            for j, connected in enumerate(isConnected[i]):
                if connected and not visited[j]:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                province_count += 1
        
        return province_count


    def func2(self, connect_mat):
        if not connect_mat:
            return 0
        N = len(connect_mat)
        visited = [False]*N
        cluster_cnt = 0

        def dfs(city_id):
            visited[city_id] = True
            for j, isConnect in enumerate(connect_mat[city_id]):
                if isConnect==1 and visited[j] == False:
                    dfs(j)

        for i in range(N):
            if visited[i] == False:
                dfs(i)
                cluster_cnt += 1

        return cluster_cnt


if __name__ == "__main__":
    # Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]], Output: 2
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    sol = Solution()
    print("solu-1: ", sol.findCircleNum(isConnected))
    print("solu-2: ", sol.func2(isConnected))

    # Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]], Output: 3
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print("solu-1: ", sol.findCircleNum(isConnected))
    print("solu-2: ", sol.func2(isConnected))