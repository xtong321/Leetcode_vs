"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Idea:
解题思路
定义“可整除”： 对于字符串 s 和 t，如果 s 可以由若干个 t 拼接而成，则称 t 整除 s。 例如 "ABCABC" 可以被 "ABC" 整除。

判断是否存在公共因子子串：
如果 str1 + str2 != str2 + str1，说明两者没有公共因子子串，直接返回 ""。
否则，说明存在公共因子子串。
利用数学最大公约数：
公共因子子串的长度一定是 gcd(len(str1), len(str2))。
因为只有长度能同时整除两个字符串长度时，才能保证重复拼接后完全覆盖。
取前缀作为答案：
答案就是 str1[:gcd(len(str1), len(str2))]。
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 如果拼接结果不同，说明不存在公共因子子串
        if str1 + str2 != str2 + str1:
            return ""
        # 否则取长度的最大公约数对应的前缀
        #gcd_len = math.gcd(len(str1), len(str2))
        gcd_len = self.gcd(len(str1), len(str2))
        return str1[:gcd_len]

    # find gcd of 2 num
    def gcd(self, num1, num2):
        if num1<=0 or num2<=0:
            return 0
        min_num = min(num1, num2)

        start = min_num
        for i in range(min_num, 0, -1):
            if num1 % i == 0 and num2 % i ==0:
                return i

        return 1

if __name__ == "__main__":
    str1 = 'ABCABC'
    str2 = 'ABC'
    print(Solution().gcdOfStrings(str1, str2))

    str1 = 'ABABAB'
    str2 = 'AB'
    print(Solution().gcdOfStrings(str1, str2))