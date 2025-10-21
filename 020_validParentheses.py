"""
原题
判断一个只包含各种括号符号的字符串中括号的匹配情况。
注意点：
字符串中只会包含"(",")","[","]","{","}"这些字符
括号匹配要注意顺序，字符串"([)]"是错误的匹配
例子：
输入: s="(){}" 输出: True
输入: s="(){}[" 输出: False
解题思路
典型的用栈来解决的问题，遇到左括号就压栈，遇到右括号时如果栈为空（类
似"]]]"的情况），则失败，否则取栈顶元素，看两个括号是否匹配。如果最后栈不
为空（类似"[[["的情况），则匹配失败。
"""

class Solution:
    def isValid(self, str_s):
        if len(str_s) % 2 != 0:
            return False

        while '()' in str_s or '[]' in str_s or '{}' in str_s:
            str_s = str_s.replace('()', '')
            str_s = str_s.replace('[]', '')
            str_s = str_s.replace('{}', '')
        
        if len(str_s) == 0:
            return True
        else:
            return False

    def isValid2(self, str_s):
        if len(str_s) % 2 != 0:
            return False
        
        res = []
        for char in str_s:
            if char == '(' or char == '[' or char == '{':
                res.append(char)
            else:
                if len(res) == 0:
                    return False
                if char == ')' and res[-1]!='(' or char == ']' and res[-1]!='[' or char == '}' and res[-1]!='{':
                    return False

                res.pop()

        if len(res) != 0:
            return False

        return True



if __name__ == "__main__":
    print(Solution().isValid("([{}])"))
    print(Solution().isValid("()[{}])("))
    print(Solution().isValid2("([{}])"))
    print(Solution().isValid2("()[{}])("))
