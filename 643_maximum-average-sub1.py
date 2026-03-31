"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n 
elements, and an integer k.
Find a contiguous subarray whose length is equal to 
k that has the maximum average value and return 
this value. Any answer with a calculation error 
less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Idea:
1) usa a sliding window to enclose a subarray to get sum
2) slide the window, compare the new enter number and removed
   number to check if the sub-sum become bigger
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or len(nums) < k:
            return None
        N = len(nums)
        if N <= k:
            return sum(nums)/N
        start = 0
        end = start + k
        sub_sum = 0
        
        #initial value
        sub_sum = sum(nums[start:end])
        opt_start, opt_end, opt_sum = 0, k-1, sub_sum

        for start in range(1, N-k):
            end = start+k-1
            if nums[end] > nums[start-1]:
                sub_sum += (nums[end] - nums[start-1])
                if opt_sum < sub_sum:
                    opt_sum = sub_sum
                    opt_start = start
                    opt_end = end
        
        opt_sum /= k

        return [opt_start, opt_end, opt_sum]


if __name__ == "__main__":
    nums, k = [1,12,-5,-6,50,3], 4 # Output: 12.75000
    print(Solution().findMaxAverage(nums, k))

    nums, k = [5], 1 # Output: 5.00000
    print(Solution().findMaxAverage(nums, k))