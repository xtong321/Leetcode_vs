"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(nums):
            return -1

        # size of original array
        N = len(nums) 

        # size of result array
        L = N - k + 1

        res = [0 for _ in range(L)]
        for i in range(0, N-k+1):
            start = i
            end = i + k -1
            sub_array = nums[start:end+1]
            res[i] = max(sub_array)

        return res

    def maxSlidingWindow2(self, nums, k):
        win, ret = [], []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.pop(0)

            while win and nums[win[-1]] <= v:
                win.pop()

            win.append(i)

            if i >= k - 1: 
                ret.append(nums[win[0]])

        return ret

if __name__ == "__main__":
    print(Solution().maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]