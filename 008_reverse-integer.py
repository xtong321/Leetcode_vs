"""
原题
翻转一个intger类型的数字。
注意点：
注意末尾有0的情况不能直接当作字符串翻转
有正负两种情况
integer是32位整型，考虑溢出
例子：
输入: x=123 输出: 321
输入: x=-123 输出: -321
解题思路
由于Python可以支持几乎无限大的数，直接把末尾的数不断添加到目标书中即可。
最后再处理溢出的情况。如果想通过转换为字符然后翻转的方法来实现，需要把末
尾的0先去掉。
AC源
"""

class Solution(object):
    def reverse(self, x):
        flag = 0
        if x<0:
            flag = -1
        else:
            flag = 1

        result = 0
        x = x * flag
        while x>0:
            result = result * 10 + x % 10
            x = x // 10

        if result > 2147483647:
            return 0
        else:
            return result * flag

        return result


if __name__ == "__main__":
    print(Solution().reverse(321000))
    print(Solution().reverse(-321))
    print(Solution().reverse(123))
    #assert Solution().reverse(321000) == 123
    #assert Solution().reverse(-321) == -123
    #assert Solution().reverse(1534236469) == 0




