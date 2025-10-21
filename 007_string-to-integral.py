"""
讲一个字符串转化成int类型。题目非常简单，但要额外考虑的因素非常多，如下面
的一些字符串的处理："+123", " -23 ", "231ji2", null, " "等等。
注意点：
字符串可能为空
字符串可能全是空格，或前后有空格
要考虑正负号
要考虑对于32位整数是否溢出
要考虑不是数字的字符，如果首字母不是数字，返回为0，在字符串中的将它
及它之后的字符全部忽略
异常情况全部返回0
例子：
输入: str=" +123" 输出: 123
输入: str="-123fe2" 输出: -123
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        007 String to Integer (atoi)
        26
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if not str:
            return 0

        # check space
        str = str.strip()
        if not str:
            return 0

        # check flag
        flag = 1
        if str[0] in ['+', '-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]

        # check non
        if not str or not str[0].isdigit():
            return 0
        
        # Ignore all char after the first no-number char
        for i, v in enumerate(str):
            if not v.isdigit():
                str = str[:i]
                break
        result = 0
        for v in str[:]:
            result += ord(v) - ord('0')
            result *= 10
        result /= 10
        result *= flag
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return int(result)
        
        
if __name__ == "__main__":
    print(Solution().myAtoi(" -1123")) # == -1123
    print(Solution().myAtoi("+4321")) # == 4321
    print(Solution().myAtoi("222222222222222")) # == 2147483647
