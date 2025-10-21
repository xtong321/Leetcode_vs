"""
给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff 。
找出满足下述条件的下标对 (i, j)：
i != j,
abs(i - j) <= indexDiff
abs(nums[i] - nums[j]) <= valueDiff
如果存在，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
输出：true
解释：可以找出 (i, j) = (0, 3) 。
满足下述 3 个条件：
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

示例 2：
输入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
输出：false
解释：尝试所有可能的下标对 (i, j) ，均无法满足这 3 个条件，因此返回 false 
"""

class Solution(object):
    def func(self, nums, idxDiff, valDiff):
        '''
        construct a matirx to store elem-diff
        find values that meet these conditions
        '''
        N = len(nums)
        # mat = [[0] for _ in range(N)]
        #mat = [[0]*N]*N
        mat = [[0 for j in range(N)] for i in range(N)]
        for i in range(N-1):
            for j in range(i+1, N):
                mat[i][j] = abs(nums[i] - nums[j])
                mat[j][i] = mat[i][j]
        
        ans = []
        for diag in range(N):
            for i in range(max([0, diag-idxDiff]), min([diag+idxDiff+1, N])):
                if diag == i:
                    continue
                if mat[diag][i] == valDiff:
                    ans.append([diag, i])

        return ans

    def func2(self, nums, k, t):
        ls = [[nums[i], i] for i in range(len(nums))] # combine [val, idx]
        ls.sort(key=lambda x: x[0]) # sort and then compare
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ls[j][0] - ls[i][0] > t:
                    break
                if abs(ls[j][1] - ls[i][1]) <= k:
                    return True
        return False

if __name__ == "__main__":
    nums, indexDiff, valueDiff = [1,2,3,1], 3, 0
    print(Solution().func(nums, indexDiff, valueDiff)) # (i, j) = (0, 3)

    nums, indexDiff, valueDiff = [1,5,9,1,5,9], 2, 3
    print(Solution().func(nums, indexDiff, valueDiff)) # None
