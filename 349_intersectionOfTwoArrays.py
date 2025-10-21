"""
描述：给定两个数组 nums1 和 nums2。
要求：返回两个数组的交集。重复元素只计算一次。
说明：
1≤nums1.length, nums2.length≤1000。
0≤nums1[i],nums2[i]≤1000。

示例：
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

Idea:
1) build a hashmap for num1
2) check num2 if there is existed elements
3) aggragate repeated elements
"""

class Solution(object):
    def func2(self, nums1, nums2):
        if not nums1 or not nums2:
            return None

        N1 = len(nums1)
        N2 = len(nums2)
        num_map = {}
        for i in range(N1):
            if nums1[i] in num_map:
                continue
            num_map[nums1[i]] = nums1[i]

        intersect_list = []
        for j in range(N2):
            if nums2[j] in num_map and nums2[j] not in intersect_list:
                intersect_list.append(nums2[j])

        return intersect_list
        #return list(set(intersect_list))

    def func2(self, nums1, nums2):
        """
        :1) merge nums1 and nums2
        :2) sort
        :3) scan if there is repeated elements
        """
        if not nums1 or not nums2:
            return None
        
        nums = nums1 + nums2
        nums.sort()

        intersect_list = []
        N = len(nums)
        i = 0
        while i < N-1:
            only_once = 0
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                if only_once==0:
                    intersect_list.append(nums[i])                    
                only_once += 1
                i += 1
            i += 1

        return intersect_list

    def func3(self, nums1, nums2):
        """
        :1) sort 2 nums
        :2) use 2 pointers to scan from left to right to get repeated elements
        """
        if not nums1 or not nums2:
            return None
        
        nums1.sort()
        nums2.sort()
        left1 = 0
        left2 = 0
        ans = []
        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                if nums1[left1] not in ans:
                    ans.append(nums1[left1])
                left1 += 1
                left2 += 1
            elif nums1[left1] < nums2[left2]:
                left1 += 1
            elif nums1[left1] > nums2[left2]:
                left2 += 1

        return ans


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().func3(nums1, nums2)) # output: [2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().func3(nums1, nums2)) # output: [9,4] or [4,9]