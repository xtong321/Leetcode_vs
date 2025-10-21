"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You may assume that A has enough space (size that is greater or equal
to m + n) to hold additional elements from B. The number of elements
initialized in A and B are m and n respectively.
A和B都已经是排好序的数组，我们只需要从后往前比较就可以了。
因为A有足够的空间容纳A + B，我们使用游标i指向m + n - 1，也就是最大数值存放
的地方，从后往前遍历A，B，谁大就放到i这里，同时递减i。
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = m + n -1
        m = m-1
        n = n-1
        while(index>=0 & m>=0 & n>=0):
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m = m-1
            else:
                nums1[index] = nums2[n]
                n = n-1

            index = index - 1

        if n>=0:
            nums1[:n+1] = nums2[:n+1]

        return nums1
    
if __name__ == "__main__":
    """
    assert Solution().merge(
    [1, 1, 2, 2, 4, 0, 0, 0, 0], m=5
    [0, 0, 2, 3], n=4)
    """
    print(Solution().merge(
    [1, 1, 2, 2, 4, 0, 0, 0, 0], 5,
    [0, 0, 2, 3], 4))
