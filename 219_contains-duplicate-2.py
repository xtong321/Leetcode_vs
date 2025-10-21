"""
描述：给定一个整数数组 nums 和一个整数 k。
要求：判断是否存在 nums[i]==nums[j]（i ≠ j），并且 i 和 j 的差绝对值至多为 k。

说明：
示例 1：
输入：nums = [1,2,3,1], k = 3
输出：True
"""

class Solution():
    def containDup2(self, nums, k):
        dic = {}
        if len(nums)<k:
            return False

        for i, num in enumerate(nums):            
            if num in dic and i-dic[num] <= k:
                return True
            dic[num] = i

        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k1=2
    k2=3
    k3=4
    print(Solution().containDup2(nums, k1))
    print(Solution().containDup2(nums, k2))
    print(Solution().containDup2(nums, k3))

    rows_map = [1 for _ in range(9)]
    print(rows_map)