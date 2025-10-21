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
def twoSum1(nums, target):
    hash_map = {}
    for index, value in enumerate(nums):
        hash_map[value] = index
    for index1, value in enumerate(nums):
        if target - value in hash_map:
            index2 = hash_map[target - value]
            if index1 != index2:
                return [index1, index2]

def twoSum2(nums, target):
    hash_map = {}
    #for index, value in enumerate(nums):
    #    hash_map[value] = index
    
    for index1, value in enumerate(nums):
        if target - value in hash_map:
            index2 = hash_map[target - value]
            if index1 != index2:
                return [index1, index2]
        hash_map[value] = index1
    return []
    '''hash_res = {}
    for k, v in enumerate(nums):
        if target - v in hash_res:
            return [hash_res[target - v], k]
        hash_res[v] = k
    return []
    '''

# date = 2025/10/02
def twoSum3(nums, target):
    if not nums:
        return None
    num_dict = {}
    for idx1, num1 in enumerate(nums):
        num_dict[num1] = idx1
        if target - num1 in num_dict:
            idx2 = num_dict[target - num1]
            if idx1 != idx2:
                return [idx1, idx2]
    return None    


# main function
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print("nums = {}, target = {}".format(nums, target))

    idx11, idx12 = twoSum1(nums=nums, target=target)
    print("solu-1: idx = {},{}".format(idx11, idx12))

    idx21, idx22 = twoSum2(nums=nums, target=target)
    print("solu-2: idx = {},{}".format(idx21, idx22))

    idx31, idx32 = twoSum3(nums=nums, target=target)
    print("solu-2: idx = {},{}".format(idx31, idx32))
    
    #print("nums = %s" % nums)
    #print("idx = %d, %d; target = %d" % (idx1, idx2, target))



