"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<=1:
            return 0

        # original window that contain at most 1 zero (0 or 1 zero), []
        org_start, org_end = 0, 0
        # extend window to left and right that all neighbor elements are zero, []
        ext_start, ext_end, ext_size = 0, 0, 0
        # optimal result
        opt_start, opt_end, opt_size = 0, 0, 0
        N = len(nums)

        # if all elem are 1
        if nums.count(0) <= 1:
            return [0, N-1, N-1]

        while ext_end < N-1:
            # find org_win
            for org_end in range(N-1, org_start, -1):
                sub_nums = nums[org_start:org_end+1]
                if sub_nums.count(0) <= 1:                    
                    break
                
            # find ext_win, extend to left and right
            ext_start, ext_end = org_start, org_end
            for offset in range(1, org_start):
                if org_start - offset >= 0 and nums[org_start - offset] == 1:
                    continue
                else:
                    ext_start = org_start - offset + 1
                    break
            for offset in range(1, N-org_end):
                if nums[org_end + offset] == 1:
                    continue
                else:
                    ext_end = org_end + offset - 1
                    break
            
            ext_size = ext_end - ext_start # []
            if opt_size < ext_size:
                opt_size = ext_size
                opt_start = org_start
                opt_end = org_end

            org_start += 1
        
        return [opt_start, opt_end, opt_size]        
        # raise NotImplementedError


if __name__ == "__main__":
    nums = [1,1,0,1] # Output: 3, remove the 2nd element
    print(Solution().longestSubarray(nums))

    nums = [0,1,1,1,0,1,1,0,1] # Output: 5, remove the 4th element
    print(Solution().longestSubarray(nums))

    nums = [1,1,1] # Output: 2, Explanation: You must delete one element.
    print(Solution().longestSubarray(nums))
        

