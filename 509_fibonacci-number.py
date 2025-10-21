"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。

示例 1：
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
"""

class Solution(object):    
    # Dynamic Programming
    def fabonacci(self, n):
        if n==0:
            return 0

        if n==1:
            return 1
        
        F = [0 for _ in range(n+1)]
        F[0] = 0
        F[1] = 1        

        for k in range(2, n+1):
            F[k] = F[k-1] + F[k-2]

        return F[n]

    #resurive solution
    def fabonacci2(self, n):
        if n==0:
            return 0

        if n==1:
            return 1
        
        Fn = self.fabonacci2(n-1) + self.fabonacci2(n-2)

        return Fn

# memoization solution
class Solution2:
    def fib(self, n: int) -> int:
        # 使用数组保存已经求解过的 f(k) 的结果
        memo = [0 for _ in range(n + 1)]
        return self.my_fib(n, memo)

    def my_fib(self, n, memo):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # 已经计算过结果
        if memo[n] != 0:
            return memo[n]
        
        # 没有计算过结果
        memo[n] = self.my_fib(n - 1, memo) + self.my_fib(n - 2, memo)
        return memo[n]

if __name__ == "__main__":
    print("Fab({}) = {} ".format(2, Solution().fabonacci2(2)))
    print("Fab({}) = {} ".format(5, Solution().fabonacci2(5)))
    print("Fab({}) = {} ".format(6, Solution().fabonacci2(6)))