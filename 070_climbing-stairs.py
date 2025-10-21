"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""

class Solution(object):
    def climb(self, N):
        if N<=1:
            return N
        
        F = [0 for _ in range(N+1)]
        F[0] = 1
        F[1] = 1        
        for k in range(2, N+1):
            F[k] = F[k-1] + F[k-2]

        return F[N]


if __name__ == "__main__":
    #test cases
    Test = [
        [1,1], 
        [2,2], 
        [3,3], 
        [4,5]
        ]
    for i in range(0, len(Test)):
        print("F({}) = {}, answer is {} ".format(Test[i][0], Solution().climb(Test[i][0]), Test[i][1]))
        