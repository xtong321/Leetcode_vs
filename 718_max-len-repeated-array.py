"""
描述：给定两个整数数组 nums1、nums2。
要求：计算两个数组中公共的、长度最长的子数组长度。

说明：
1≤nums1.length,nums2.length≤1000。
0≤nums1[i],nums2[i]≤100。

示例：
示例 1：
输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。

示例 2：
输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5

solution:
1) DP problem
2) define dp[i][j] 为 num1 中以 i 结尾的子数组，和 num2 中以 j 结尾的子数组的最长公共子数组

状态转移方程：
1) dp[i][j] = dp[i-1][j-1] + 1, if num1[i-1] == num2[j-1]
2) otherwise, dp[i][j] = 0
3) return max_len
"""

class solution():
    def maxRepeatArray(self, num1, num2):
        size1 = len(num1)
        size2 = len(num2)
        dp = [ [0 for _ in range(size2+1)] for _ in range(size1+1) ]
        max_len= 0
        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if num1[i-1] == num2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    #dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    dp[i][j] = 0

                if max_len < dp[i][j]:
                    max_len = dp[i][j]

        return max_len

if __name__ == "__main__":
    print(solution().maxRepeatArray([1,2,3,2,1], [3,2,1,4,7]))
    print(solution().maxRepeatArray([1,2,3,2,5,1], [3,2,1,4,7]))
    print(solution().maxRepeatArray([1,2,3,4], [3,2,1,4,7]))
    print(solution().maxRepeatArray([1,2,3,0], [1,2,3,0,0,1,2,3,0]))