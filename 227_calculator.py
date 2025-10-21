"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：
1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
题目数据保证答案是一个 32-bit 整数
"""

class Solution:
    def calculate(self, str): # return int (-> int:)
        if len(str) <= 0:
            print("Error! no str input")
            return
        
        # use a list to store number to be calculate, operator is ‘add’
        size = len(str)
        index = 0   #index of char in str
        num_str = []
        op = '+'
        num = 0 # convert from str to num
        while index < size:
             # multi-num?
            if str[index].isdigit():
                num = int(str[index]) # multi-digit num
                while index+1 < size and str[index+1].isdigit():
                    num = num*10 + int(str[index+1])
                    index += 1

                if op == '+':
                    num_str.append(num)
                elif op == '-':
                    num_str.append(-num)
                elif op == '*':
                    num_a = num_str.pop()                    
                    num_str.append(num*num_a)
                elif op == '/':
                    num_a = num_str.pop()                    
                    num_str.append(int(num_a/num))
            elif str[index] in "+-*/":
                op = str[index]
            index += 1
        
        res = sum(num_str)
        return res










    def cal2(self, s):
        size = len(s)
        stack = []
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                num = ord(s[index]) - ord('0')
                while index + 1 < size and s[index+1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                op = s[index]
            index += 1

        return sum(stack)


if __name__ == "__main__":
    print(Solution().calculate("-13+4*5"))