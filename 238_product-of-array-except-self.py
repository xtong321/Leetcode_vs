"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Idea:
标准解法是用 前缀积 + 后缀积 的思路：先计算每个位置左边所有数的乘积，再乘以右边所有数的乘积。这样就能得到除自身以外的乘积。

解题思路
前缀积：
从左到右遍历，prefix[i] 表示 nums[0..i-1] 的乘积。
即 prefix[i] = prefix[i-1] * nums[i-1]。

后缀积：
从右到左遍历，suffix[i] 表示 nums[i+1..n-1] 的乘积。
即 suffix[i] = suffix[i+1] * nums[i+1]。

结果：
对于每个位置 i，结果是 prefix[i] * suffix[i]。
空间优化：
可以直接用结果数组存储前缀积，再用一个变量保存后缀积，边遍历边更新，做到 O(1) 额外空间。
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        if nums.count(0) >= 2:
            return 0*nums

        N = len(nums)
        res = [0]*N

        prefix = 1
        suffix = 1
        
        #prefix
        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]

        #suffix
        for i in range(N-1, -1, -1):            
            res[i] *= suffix
            suffix *= nums[i]

        return res

    """
    idea:
    1) compute the product of all items
    2) for each item specific product, use the all_product to divide this item
    """
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]        
        """
        if not nums:
            return nums

        # if #(0) >= 2
        if nums.count(0) >= 2:
            return 0*nums

        N = len(nums)
        res = [0]*N
        all_product = 1

        # if #(0) = 1
        if nums.count(0) == 1:
            for i in range(N):
                if nums[i] != 0:
                    all_product *= nums[i]

            for i in range(N):
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = all_product

            return res
        
        # otherwise
        for i in range(N):
            all_product *= nums[i]

        for i in range(N):
            res[i] = int(all_product/nums[i])

        return res

if __name__ == "__main__":
    nums = [1,2,3,4] #Output: [24,12,8,6]
    print(Solution().productExceptSelf2(nums))

    nums = [-1,1,0,-3,3] #Output: [0,0,9,0,0]
    print(Solution().productExceptSelf2(nums))