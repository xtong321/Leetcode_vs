"""
目大意
描述：给定一个只包含正整数的数组 nums 和一个正整数 target。
要求：找出数组中满足和大于等于 target 的长度最小的「连续子数组」，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1
"""
class Solution:
    def minSubArrayLen(self, target, nums):
        if sum(nums) < target:
            return 0

        size = len(nums)
        left = 0
        right = 0
        sub_sum = 0
        sub_nums = [] # returned sub-array
        res = size + 1
        res_nums = []

        while right < len(nums):
            if nums[right] > target:
                right += 1
                continue
            sub_sum += nums[right]
            sub_nums.append(nums[right])

            while sub_sum > target and left < right and sub_sum - nums[left] >= target:
                sub_sum -= nums[left]
                sub_nums.remove(nums[left])
                left += 1
                #sub_nums.pop(nums[right])

            if sub_sum == target:
                res = min(res, right-left+1)
                res_nums = list(sub_nums) # or sub_nums[:]

            right += 1

        #return res if res != size + 1 else 0
        if res!= size+1:
            return res, res_nums
        else:
            return 0, None


if __name__ == "__main__":
    print(Solution().minSubArrayLen(19, [1,3,1,10,4,3]), 'target =', 19)
    print(Solution().minSubArrayLen(16, [1, 4, 2, 3, 8, 5]), 'target =', 16)