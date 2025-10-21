"""
描述：给定一个数组 nums，nums[i] 代表第 i 间房屋存放的金额。相邻的房屋装有防盗系统，假如相邻的两间房屋同时被偷，系统就会报警。
要求：假如你是一名专业的小偷，计算在不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。

说明：
1≤nums.length≤100。
0≤nums[i]≤400。

示例：
示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12。
"""

class solution():
    def maxSum(self, nums):
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        if size == 2:
            return max(nums[0], nums[1])

        dp = nums
        for i in range(2, size):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return max(dp)


if __name__ == "__main__":
    print(solution().maxSum([1,2,3,1])) # 4
    print(solution().maxSum([2,7,9,3,1])) # 12