"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

class Solution(object):
    def minPathSum(self, grid): # grid: List[List[int]] -> int
        if not grid or not grid[0]:
            return 0
        
        row = len(grid)
        col = len(grid[0])

        # 1. create dp array 
        dp = [[0] * col for _ in range(row)]

        # 处理边界情况
        # 2. 设置起始点
        dp[0][0] = grid[0][0]

        # 3. 初始化第一列
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # 4. 初始化第一行
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        
        # 5. 填充剩余的 dp 数组
        for i in range(1, row):
            for j in range(1, col):
                #dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1]) + grid[i][j] # only right and down allowed
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1]) + grid[i][j] # (right, down, rightdown) allowed
        
        return dp[row - 1][col - 1]


if __name__ == "__main__":
    grid = [[1,3,4],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))


"""
C++
public int minPathSum(int[][] grid) {
        int width = grid[0].length, high = grid.length;
        if (high == 0 || width == 0) return 0;
        // 初始化
        for (int i = 1; i < high; i++) grid[i][0] += grid[i - 1][0];
        for (int i = 1; i < width; i++) grid[0][i] += grid[0][i - 1];
        for (int i = 1; i < high; i++)
            for (int j = 1; j < width; j++)
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        return grid[high - 1][width - 1];
    }
"""