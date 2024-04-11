"""
001 - two sum
给一个int型数组，要求找出其中两个和为特定值的数的坐标。
注意点：
返回的坐标一要比坐标二小
最小的坐标是1，不是0
例子：
输入: numbers={2, 7, 11, 15}, target=9 输出: index1=1, index2=2

https://leetcode.cn/problems/two-sum/description/
"""


"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
def twoSum(nums, target):
    hash_map = {}
    for index, value in enumerate(nums):
        hash_map[value] = index
    for index1, value in enumerate(nums):
        if target - value in hash_map:
            index2 = hash_map[target - value]
            if index1 != index2:
                return [index1 + 1, index2 + 1]






def twoSum2(nums, target):
    hash_map = {}
    for index, value in enumerate(nums):
        hash_map[value] = index
    for index1, value in enumerate(nums):
        if target - value in hash_map:
            index2 = hash_map[target - value]
            if index1 != index2:
                return [index1+1, index+2]



# main function
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    #idx1, idx2 = twoSum(nums=nums, target=target)
    idx1, idx2 = twoSum2(nums=nums, target=target)
    print("nums = {}".format(nums))
    #print("nums = %s" % nums)
    print("target = {}".format(target))
    print("idx = {},{}".format(idx1, idx2))
    #print("idx = %d, %d" % (idx1, idx2))



