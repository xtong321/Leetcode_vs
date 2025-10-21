"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回: 你可以获得的最大乘积 。

示例 1:
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""

class solution():
    def fun1(self, N):
        if N<=1:
            return 0
        if N==2:
            return 1

        dp = [0 for _ in range(N+1)]
        ans = 0

        for i in range(3, N+1):
            for j in range(2, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j], dp[j]*(i-j), dp[j]*dp[i-j])
                #dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

                ans = max(ans, dp[i])

        return dp[N]

    def fun2(self, N):
        if N<=1:
            return 0
        if N==2:
            return 1
        if N==3:
            return 2
        if N==4:
            return 4

        ans = 1
        while N>4:
            N = N - 3
            ans = ans * 3

        ans = ans * N

        return ans

if __name__ == "__main__":
    print(solution().fun2(2)) # 1
    print(solution().fun2(10)) # 36