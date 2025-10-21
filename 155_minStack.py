"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
 

示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
import math

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = math.inf
        self.minStack = [] # to save min element

    def push(self, val):
        self.stack.append(val)
        self.min = min(self.min, val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            if self.minStack[-1] == self.stack[-1]:
                self.minStack.pop()
            self.stack.pop()
                

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.minStack[-1]
        

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(4)
    minStack.push(5)
    minStack.push(1)
    minStack.push(3)
    print(minStack.getMin()) # == 1
    minStack.pop()
    minStack.pop()
    print(minStack.top()) # == 5