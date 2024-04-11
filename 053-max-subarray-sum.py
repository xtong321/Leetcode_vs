"""
https://leetcode.cn/problems/maximum-subarray/

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组
是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
"""

class Solution(object):
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        current = nums[0]
        m = current
        for i in range(1, length):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        return m
        
if __name__ == '__main__':
    #nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [5,4,-1,7,8]
    print(Solution().maxSubArray(nums))