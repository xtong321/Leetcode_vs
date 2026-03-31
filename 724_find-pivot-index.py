"""
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Idea:
1) compute accumulate sum as a new array
2) scan pivot from start to end
3) left_sum = ..., right_sum = all_sum - left_sum - cur_val
"""

class Solution(object):
    def pivotIndex(self, nums):
        if not nums:
            return None
        N = len(nums)
        accu_sum_arr = [nums[0]] * N
        for i in range(1, N):
            accu_sum_arr[i] = accu_sum_arr[i-1] + nums[i]

        pivot_idx = -1
        left_sum, right_sum = 0, 0
        all_sum = accu_sum_arr[N-1]
        for idx in range(0, N):
            if idx == 0:
                left_sum = 0
            else:
                left_sum = accu_sum_arr[idx-1]
            right_sum = all_sum - left_sum - nums[idx]
            if left_sum == right_sum:
                return idx
        
        return -1


if __name__ == "__main__":
    nums = [1,7,3,6,5,6] # Output: 3
    print(Solution().pivotIndex(nums))

    nums = [1,2,3] # Output: -1
    print(Solution().pivotIndex(nums))

    nums = [2,1,-1] # Output: 0
    print(Solution().pivotIndex(nums))