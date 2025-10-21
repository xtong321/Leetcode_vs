"""
描述：给定两个数组 nums1 和 nums2。
要求：返回两个数组的交集。可以不考虑输出结果的顺序。
说明：
输出结果中，每个元素出现的次数，应该与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
1≤nums1.length,nums2.length≤1000。
0≤nums1[i],nums2[i]≤1000。

示例：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""

class Solution:
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return None

        numDict = {}
        ans = [] # return target list
        for i in range(len(nums1)):
            if nums1[i] in numDict:
                numDict[nums1[i]] += 1
            else:
                numDict[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in numDict and numDict[nums2[i]] != 0:
                numDict[nums2[i]] -= 1
                ans.append(nums2[i])
            
        return ans


if __name__ == "__main__":
    nums1, nums2 = [1,2,2,1], [2,2]
    print(Solution().intersect(nums1, nums2)) # [2,2]

    nums1, nums2 = [4,9,5], [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2)) # [4,9]
