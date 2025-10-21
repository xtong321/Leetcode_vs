"""
median-of-two-sorted-arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution(object):
    def func1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        :Idea: 1) one pointer to each nums, and insert one by one
        """
        if not nums1 and not nums2:
            return None        
        if nums2 and not nums1:
            N = len(nums2)
            if N % 2 == 0:
                return (nums2[N//2-1] + nums2[N//2])/2
            else:
                return nums2[N//2]
        if nums1 and not nums2:
            N = len(nums1)
            if N % 2 == 0:
                return (nums1[N//2-1] + nums1[N//2])/2
            else:
                return nums1[N//2]

        N1 = len(nums1)
        N2 = len(nums2)
        p1 = 0
        p2 = 0
        nums = []
        while p1 < N1 and p2 < N2:
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:                
                nums.append(nums2[p2])
                p2 += 1
        if p1>=N1 and p2<N2:
            for i in range(p2, N2):
                nums.append(nums2[i])
        if p2>=N2 and p1<N1:
            for i in range(p1, N1):
                nums.append(nums1[i])

        N = len(nums)
        if N % 2 == 0:
            return (nums[N//2-1] + nums[N//2])/2
        else:
            return nums[N//2]
                

if __name__ == "__main__":
    #nums1 = [1,3], nums2 = [2], Output: 2.00000
    #nums1 = [1,2], nums2 = [3,4], Output: 2.50000
    nums1 = [1,3]
    nums2 = [2]
    print(Solution().func1(nums1, nums2)) # 2

    nums1 = [1,2]
    nums2 = [3,4]
    print(Solution().func1(nums1, nums2)) # 2.5
