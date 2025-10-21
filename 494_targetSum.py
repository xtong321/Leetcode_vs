"""
描述：给定一个整数数组 nums 和一个整数 target。数组长度不超过 20。向数组中每个整数前加 + 或 -。然后串联起来构造成一个表达式。
要求：返回通过上述方法构造的、运算结果等于 target 的不同表达式数目。
说明：
1 ≤ nums.length ≤ 20。
0 ≤ nums[i] ≤ 1000。
0 ≤ sum(nums[i]) ≤ 1000。
−1000 ≤ target ≤ 1000。

示例：
示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：
输入：nums = [1], target = 1
输出：1
"""

class Solution():
    def targetSum(self, nums, target): # return a list containing "+,-"
        size = len(nums)

        def dfs(i, cur_sum):
            if i == size:
                if cur_sum == target:
                    return 1
                else:
                    return 0

            ans = dfs(i+1, target - nums[i]) + dfs(i+1, target + nums[i])
            return ans

        return dfs(0, 0)

    # with memorization
    def targetSum2(self, nums, target): # return a list containing "+,-"
        size = len(nums)
        table = dict()

        def dfs(i, cur_sum):
            if i == size:
                if cur_sum == target:
                    return 1
                else:
                    return 0

            if (i, cur_sum) in table:
                return table[(i, cur_sum)]

            ans = dfs(i+1, target - nums[i]) + dfs(i+1, target + nums[i])
            table[(i, cur_sum)] = ans
            return ans

        return dfs(0, 0)