"""
原题
判断一个int型数字是否是回文形式，不许用额外的空间。
注意点：
负数都是不回文数
不许用额外的空间
例子：
输入: x=123 输出: False
输入: x=12321 输出: True
"""

class Solution(object):
    def palind(self, x):
        result = True
        if x < 0:
            return False
        size = 1
        y = x
        while y>=10:
            y = y // 10
            size *= 10

        while x>0:
            head = x // size
            tail = x % 10            
            x = (x - head*size) // 10
            size /= 100
            if head != tail:
                return False

        return True

if __name__ == "__main__":
    print(Solution().palind(123))
    print(Solution().palind(12321))
    print(Solution().palind(123321))
    m=2
    n=3
    dp = [[False for i in range(n + 1)] for i in range(m + 1)]
    print(dp)



