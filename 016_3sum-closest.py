"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = []
        i = 0
        opt_ans = 100000
        opt_nums = []
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j<k:
                tri = [nums[i], nums[j], nums[k]]
                ans = sum(tri)
                if opt_ans > abs(target - ans):
                    opt_ans = abs(target - ans)
                    opt_nums = tri
                
                if sum(tri) == target:
                    result.append(tri)
                    j += 1
                    k -= 1
                    # ignor repeat
                    # Ignore repeat numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum(tri) < target:
                    j += 1
                else:
                    k -= 1
            i += 1
            # Ignore repeat numbers
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return opt_nums


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums, target)) # Output: 2

    nums = [0,0,0]
    target = 1
    print(Solution().threeSumClosest(nums, target)) # Output: 0