"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number 
of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Idea:
1) use sliding window to count the continuous 1 sub-array
2) initially, find a sub-win that contain k's 0, flip and extend (left and right) to find continuous 1
3) slide the window, till end
"""

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        if nums.count(0) <= k:
            return len(nums)
        
        N = len(nums)

        # org_start and end that contain k's 0
        org_start, org_end, org_size = 0, 0, 0
        # ext_start and end after flip k'0 and continuous 1
        ext_start, ext_end, ext_size = 0, 0, 0
        # opt value
        opt_start, opt_end, opt_size = 0, 0, 0

        # find initial size
        org_start = 0
        for org_end in range(org_start+k-1, N):
            cnt_0 = nums[org_start:org_end+1].count(0)
            if cnt_0 == k:
                break
        # extend to left
        ext_start = max(0, org_start)
        while ext_start-1 >= 0 and nums[ext_start-1] == 1:
                ext_start -= 1
        ext_start = max(0, ext_start)
        # extend to right
        ext_end = min(N-1, org_end)
        while ext_end+1 < N and nums[ext_end+1] == 1:
                ext_end += 1
        ext_end = min(N-1, ext_end)
        opt_start = org_start
        opt_end = org_end
        opt_size = ext_end - ext_start + 1

        # slide window
        for org_start in range(1, N-k):
            for org_end in range(org_start+k-1, N):
                cnt_0 = nums[org_start:org_end+1].count(0)
                if cnt_0 == k:
                    break
            org_size = org_end - org_start + 1

            # ext to left/right
            ext_size = org_size
            ext_start = max(0, org_start)
            while ext_start-1 >= 0 and nums[ext_start-1] == 1:
                ext_start -= 1                
            ext_start = max(0, ext_start)

            # extend to right
            ext_end = min(N-1, org_end)
            while ext_end+1 < N and nums[ext_end+1] == 1:
                ext_end += 1
            ext_end = min(N-1, ext_end)
            ext_size = ext_end - ext_start + 1

            if opt_size < ext_size:
                opt_start = org_start
                opt_end = org_end
                opt_size = ext_size

        return [opt_start, opt_end, opt_size]


if __name__ == "__main__":
    nums, k = [1,1,1,0,0,0,1,1,1,1,0], 2 #Output: 6
    print(Solution().longestOnes(nums, k))

    nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3 # Output: 10
    print(Solution().longestOnes(nums, k))