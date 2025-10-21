"""
题目描述
实现一个函数 Pow(x, n)，该函数计算并返回 $x$ 的 $n$ 次幂（即 $x^n$）。该函数需要处理大数的情况，并且 $n$ 可能是负数。

注意：

你不能使用库函数，如 Math.pow()（JavaScript）、pow()（PHP）或 ** 运算符（Python）来直接计算幂。
负数指数幂的定义是 $x^{-n} = 1 / x^n$，其中 $x \neq 0$。
"""

class Solution(object):
    def pow(self, x, n):
        if n==0:
            return 1

        if n<0:
            n = -n
            x = 1/x

        result = 1
        half = pow(x, n//2)
        if n % 2 == 0:
            result = half * half
        else:
            result = half * half * x

        return result

if __name__ == "__main__":
    print(Solution().pow(2, 10))
    print(Solution().pow(10, -2))

