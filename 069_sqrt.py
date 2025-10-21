"""
原题
求一个数的平方根。
注意点：
结果返回整数，舍去小数，不是四舍五入
例子：
输入: x = 5
输出: 2
"""

class Solution(object):
    def Sqrt(self, x):
        if x < 0:
            return None
        if x == 1:
            return 1
        
        left = 0
        right = x
        res = -1
        mid = (left + right) % 2
        while left <= right:
            mid = left + (right-left) // 2
            if mid*mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return res

if __name__ == "__main__":
    print(Solution().Sqrt(10))
    print(Solution().Sqrt(100))