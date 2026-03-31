"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists 
a triple of indices (i, j, k) such that i < j < k and 
nums[i] < nums[j] < nums[k]. If no such indices exists, 
return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), 
because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

class Solution(object):
    def func1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)<=2:
            return False

        N = len(nums)

        prefix = False
        suffix = False
        for i in range(1, N-1):
            prefix = False
            suffix = False
            for j in range(0, i):
                if nums[i] > nums[j]:
                    prefix = True
                    break

            if not prefix:
                continue
            else:
                for k in range(i+1, N):
                    if nums[i] < nums[k]:
                        suffix = True
                        break
            
            if prefix and suffix:
                return True

        return False

    def func2(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == "__main__":
    nums = [1,2,3,4,5] #Output: true
    print(Solution().func1(nums))

    nums = [5,4,3,2,1] #Output: false
    print(Solution().func1(nums))

    nums = [2,1,5,0,4,6] #Output: true
    print(Solution().func2(nums))

        