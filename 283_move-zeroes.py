"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0] 
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        if nums.count(0) == 0:
            return nums
        
        N = len(nums)
        i = 0 #index of elem == 0
        j = 0 #index after i that != 0
        while i < N:
            if nums[i] != 0:
                i += 1
                continue
            j = i+1
            while j < N and nums[j]==0:
                j += 1
            # in case j!=0, switch
            if j < N and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        
        return nums


if __name__ == "__main__":
    nums = [0,1,0,3,12] # Output: [1,3,12,0,0]
    print(Solution().moveZeroes(nums))

    nums = [0] # Output: [0]
    print(Solution().moveZeroes(nums))