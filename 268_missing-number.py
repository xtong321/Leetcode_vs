"""
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        idea: calculate the sum of original non-missing array, and subtract the sum of 
        input array, the result is the missing number
        """
        if not nums:
            return -1 # no number missed        
        M = len(nums)
        if len(nums)+1 == max(nums):
            return -1
        sum_1 = M*(M+1)/2
        sum_2 = sum(nums)
        miss_num = int(sum_1 - sum_2)

        return miss_num

    def missingNumber2(self, nums: List[int]) -> int:
        if not nums:
            return -1 # no number missed        
        M = len(nums)
        if len(nums)+1 == max(nums):
            return -1
        ans = 0
        for i in range(len(nums)+1):
            ans ^= i
        for i, num in enumerate(nums):
            ans ^= num

        return ans


if __name__ == "__main__":
    nums = [3,0,1]; Output = 2
    print(f"{nums} miss: ", Solution().missingNumber2(nums))

    nums = [0,1]; Output = 2
    print(f"{nums} miss: ", Solution().missingNumber2(nums))

    nums = [9,6,4,2,3,5,7,0,1]; Output = 8
    print(f"{nums} miss: ", Solution().missingNumber2(nums))