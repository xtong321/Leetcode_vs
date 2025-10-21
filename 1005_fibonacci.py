"""
https://docs.pingcode.com/ask/1036513.html
fibonacci 的几种实现方法
"""

"""
1. 递归法
递归法的基本思路是将斐波那契数列的计算过程拆解为一系列子问题，并递归求解。这种方法的时间复杂度为O(2^n)，空间复杂度为O(n)。

递归法的优缺点
优点： 代码简洁，易于理解和实现。
缺点： 计算效率低，存在大量重复计算，适用于计算小规模的斐波那契数。
"""
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

"""
2. 迭代法
迭代法的基本思路是从前两个数开始，通过循环依次计算后续的斐波那契数。时间复杂度为O(n)，空间复杂度为O(1)。
迭代法的优缺点
优点： 计算效率高，适用于计算大规模的斐波那契数。
缺点： 代码略显复杂，不如递归法简洁。
"""
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a





"""
3. 记忆化递归法
记忆化递归法的基本思路是使用字典或列表缓存已计算的斐波那契数。时间复杂度为O(n)，空间复杂度为O(n)。
记忆化递归法通过在递归过程中缓存已计算的结果，避免了递归法的重复计算问题，显著提高了计算效率。

记忆化递归法的优缺点
优点： 计算效率高，代码相对简洁，适用于计算大规模的斐波那契数。
缺点： 需要额外的存储空间来缓存已计算的结果。
"""
def fibonacci_memoization(n, memo={}):
    if n in memo: # use a dict to cache previous result
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)

    return memo[n]


"""
4. 动态规划法
动态规划法通过自底向上的方式计算斐波那契数列，避免了递归法的重复计算问题，同时不需要额外的存储空间。
动态规划法的基本思路是从前两个数开始，通过循环依次计算后续的斐波那契数，并将计算结果存储在列表中。时间复杂度为O(n)，空间复杂度为O(n)。
动态规划法的优缺点
优点： 计算效率高，代码相对简洁，适用于计算大规模的斐波那契数。
缺点： 需要额外的存储空间来存储中间结果。
"""
def fibonacci_dynamic_programming(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

"""
5. 矩阵快速幂法
矩阵快速幂法是计算斐波那契数列的高级方法，通过矩阵的快速幂运算，能在对数时间内计算出结果。
矩阵快速幂法的基本思路是利用斐波那契数列的矩阵表示，通过矩阵的快速幂运算计算结果。时间复杂度为O(log n)，空间复杂度为O(1)。
矩阵快速幂法的优缺点
优点： 计算效率极高，适用于计算超大规模的斐波那契数。
缺点： 代码相对复杂，不易理解和实现。
"""
import numpy as np
def fibonacci_matrix_exponentiation(n):
    def matrix_mult(A, B):
        return np.dot(A, B)

    def matrix_power(matrix, power):
        result = np.eye(len(matrix), dtype=int)
        while power:
            if power % 2 == 1:
                result = matrix_mult(result, matrix)

            matrix = matrix_mult(matrix, matrix)
            power //= 2

        return result

    F = np.array([[1, 1], [1, 0]], dtype=int)

    return matrix_power(F, n)[0, 1]