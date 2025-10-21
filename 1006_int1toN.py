"""
check if an int array with size N includes integral from 1 to N, if yes, return 1, else return 0
"""

class Solution(object):
    def check1toN(self, N, nums):
        if len(nums) != N:
            return 0
        if min(nums) != 1 or max(nums) != N:
            return 0

        if len(nums) != len(set(nums)):
            return 0

        return 1


if __name__ == "__main__":
    print(Solution().check1toN(4, [4,3,2,1]))
    print(Solution().check1toN(4, [4,3,2,5]))
    print(Solution().check1toN(4, [4,2,2,1]))
    print(Solution().check1toN(4, [3,4,2,0, 1]))