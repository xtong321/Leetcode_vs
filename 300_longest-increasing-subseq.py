"""
描述：给定一个整数数组 nums。要求：找到其中最长严格递增子序列的长度。
说明：
子序列：由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，
[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
1≤nums.length≤2500。

示例：
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

Idea:
dp[i] is the longest increasing subseq at index [i]
state transfer program:
1) if nums[i] > nums[i-1], dp[i] = dp[i-1] + 1
2) otherwise, dp[i] = dp[i-1]

initial setting: dp[0] = 0
"""

class solution():
    def longestIncrSub(self, nums):
        if not nums:
            return 0

        size = len(nums)
        ans = 0
        dp = [1 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print(dp)
        return max(dp)

    
if __name__ == "__main__":
    print(solution().longestIncrSub(nums = [10,9,2,5,3,7,101,18])) # 4
    print(solution().longestIncrSub(nums = [0,1,0,3,2,3])) # 4