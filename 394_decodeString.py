"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。


示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (str, int) 记录左括号之前的字符串和左括号外的上一个数字
        num = 0
        res = ""  # 实时记录当前可以提取出来的字符串
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        return res


    def decodeString2(self, s: str) -> str:
        res = ""
        num = 0
        str_stack = [] # (res, num)
        for c in s:
            if c.isdigital():
                num = num*10 + int(c)
            elif c is '[':
                str_stack.append((res, num))
                res, num = '', 0
            elif c is ']':
                top = str_stack.pop()
                res = top[0] + top[1]*res
            else:
                res += c
        return res



if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))
    print(Solution().decodeString("abc3[cd]xyz"))