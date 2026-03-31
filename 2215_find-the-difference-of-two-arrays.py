"""
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Idea:
1) build hashmap for nums1 and nums2
2) check difference
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return None
        set1 = set(nums1)
        set2 = set(nums2)

        intersection = set1.intersection(set2)
        uni1 = set1.difference(intersection)
        uni2 = set2.difference(intersection)

        list1 = list(uni1)
        list2 = list(uni2)
        '''
        map1 = {}
        map2 = {}
        for i in range(0, len(set1)):
            if set1[i] not in map1:
                map1[set1[i]] = 1
        for i in range(0, len(set2)):
            if set1[2] not in map2:
                map2[set2[i]] = 1

        # check
        uni1 = []
        uni2 = []
        for i, val in enumerate(map1):
            if val not in map2:
                uni1.append(val)

        for i, val in enumerate(map2):
            if val not in map1:
                uni2.append(val)
        '''

        return [list1, list2]


if __name__ == "__main__":
    nums1, nums2 = [1,2,3], [2,4,6] # Output: [[1,3],[4,6]]
    print(Solution().findDifference(nums1, nums2))

    nums1, nums2 = [1,2,3,3],[1,1,2,2] # Output: [[3],[]]
    print(Solution().findDifference(nums1, nums2))