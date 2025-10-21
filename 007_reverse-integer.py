"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if x > 2**31 - 1 or x < -2**31:
            return 0

        flag = 1
        if x < 0:
            flag = -1

        '''
        num_digit = 1
        y = flag * x
        while y // 10 > 0:
            num_digit += 1
            y = y // 10

        num_zero = 0
        y = flag * x
        while y % 10 == 0:
            num_zero += 1
            y = y // 10
        '''

        z = 0
        y = flag * x
        while y > 0:
            res = y % 10
            z = z * 10 + res
            y = y // 10

        return z*flag

if __name__ == "__main__":
    x = 123 # Output: 321
    print(Solution().reverse(x))

    x = -123 # Output: -321
    print(Solution().reverse(x))

    x = 120 # Output: 21
    print(Solution().reverse(x))
