"""
描述：给定一个只包含 0、1 元素的二维数组，
1 代表岛屿，0 代表水。一座岛的面积就是上下左右相邻的 1 所组成的连通块的数目。
要求：计算出最大的岛屿面积。
"""

class Solution(object):
    def area(self, i, j, mat):
        if i<0 or i>=len(mat) or j<0 or j>=len(mat[0]):
            return 0
        
        count = 0
        if mat[i][j] == 1:
            count = 1
            mat[i][j] = 0
            count += self.area(i-1, j, mat)
            count += self.area(i+1, j, mat)
            count += self.area(i, j-1, mat)
            count += self.area(i, j+1, mat)
        
        return count

    def maxArea(self, mat):
        R = len(mat)
        C = len(mat[0])

        maxArea = 0
        for i in range(0, R):
            for j in range(0, C):
                if mat[i][j] == 0:
                    continue

                if mat[i][j] == 1:
                    count = 0
                    count = self.area(i, j, mat)
                    if maxArea < count:
                        maxArea = count
        return maxArea


if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxArea(grid))
