"""
描述：给定一个整数数组 nums。

要求：判断是否存在重复元素。如果有元素在数组中出现至少两次，返回 True；否则返回 False。
"""

class Solution:
    def containDuplicate_1(self, nums):
        """result = 0
        for n in nums:
            result = result ^ n
        return result==0
        """
        numDict = dict()
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = num
        return False

    """使用一个 set 集合存储数组中所有元素。
    如果集合中元素个数与数组元素个数不同，则说明出现了重复元素，返回 True。
    如果集合中元素个数与数组元素个数相同，则说明没有出现了重复元素，返回 False。
    """
    def containDuplicate_2(self, nums):
        return len(set(nums)) != len(nums)

    """
    先排序，然后看有没有相邻相等的元素
    """
    def containDuplicate_3(self, nums):
        nums.sort()
        for k in range(1, len(nums)):
            if nums[k-1] == nums[k]:
                return True
        return False

    """
    使用异或运算
    如果有相同的元素，异或应该为0， 否则为1
    只能判断连续的两个数是否相同，不能判断乱序的重复元素
    """
    def containDuplicate_4(self, nums):
        ans = 0
        for k in range(1, len(nums)):
            ans = nums[k-1]^nums[k]
            if ans == 0:
                return True
        return False
        


if __name__ == "__main__":
    print(Solution().containDuplicate_3([1, 2, 3, 4, 5]))
    print(Solution().containDuplicate_4([1, 2, 3, 4, 5]))
    print(Solution().containDuplicate_4([2, 1, 2, 3, 4, 5]))