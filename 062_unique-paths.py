"""
不同路径：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

输入：m = 3, n = 2
输出：3

输入：m = 7, n = 3
输出：28
"""

class Solution:
    def uniquePaths(self, m, n):
        if m<=1 and n<=1:
            return 1

        F = [[0 for i in range(n)] for j in range(m)]
        #print(F)
        #x3 = np.zeros((m, n), dtype=int)

        #define edge value
        for i in range(m):
            F[i][0] = 1
        for j in range(n):
            F[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                F[i][j] = F[i-1][j] + F[i][j-1]

        return F[m-1][n-1]

if __name__ == "__main__":
    Tests = [
        [3,2,3],
        [7,3,28]
    ]

    for i in range(len(Tests)):
        print("[{},{}] = {}, ans = {}".format(Tests[i][0], Tests[i][1], Solution().uniquePaths(Tests[i][0], Tests[i][1]), Tests[i][2]))
        #print(Solution().uniquePaths(7,3))

    for i, row in enumerate(Tests):
        print("[{},{}] = {}, ans = {}".format(row[0], row[1], Solution().uniquePaths(row[0], row[1]), row[2]))
        #print(Solution().uniquePaths(7,3))