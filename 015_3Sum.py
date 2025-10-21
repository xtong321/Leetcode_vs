"""
原题
找出一个列表中所有和为零的三元组。要求求出的三元组中没有重复。
注意点：
三元组中的数字要按增序排列(a<=b<=c)
结果集中没有重复的三元组
例子：
输入: nums=[-1, 0, 1, 2, -1, -4] 输出: [[-1, -1, 2], [-1, 0, 1]]
解题思路
求一个列表中所有和为零的二元组的一种思路是先把列表排序，再用两个指针从两
头向中间移动。如果前后两个数的和小于0，则左指针右移；如果和大于0，则右指
针左移。求三元组时可以参考这种做法，第一个数a确定后，可以理解为求列表中
和为-a的二元组。由于不要考虑重复的元组，遇到重复的数可以直接跳过。
"""

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        i = 0
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j<k:
                tri = [nums[i], nums[j], nums[k]]
                if sum(tri) == 0:
                    result.append(tri)
                    j += 1
                    k -= 1
                    # ignor repeat
                    # Ignore repeat numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum(tri) < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            # Ignore repeat numbers
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return result

if __name__ == "__main__":
    #assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    print(Solution().threeSum([0,0,-1, 0, 1, 2, -1, -4]))

