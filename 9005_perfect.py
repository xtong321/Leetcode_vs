"""
convert score to grade
>=90     --> A
[80, 89] --> B
[70, 79] --> C
[60, 69] --> D
<60      --> E
"""

def score_grad():
    score = float(input('input score: '))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('grade:', grade)


import random
def guess():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('pls input: '))
        if number < answer:
            print('bigger')
        elif number > answer:
            print('smaller')
        else:
            print('correct!')
            break
    print('you guess total %d times' % counter)
    if counter > 7:
        print('your IQ is too low')


def min_max():
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break

"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""
import time
import math
# start = time.clock()
start = time.process_time()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
# end = time.clock()
end = time.process_time()
print("execute time:", (end - start), "sec")
# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
# 要理解程序背后的算法 - 穷举法

#### 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    if len(x) < 2:
        print('Error: size of x smaller than 2')
        return
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    if len(x) == 2:
        return m1, m2
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def test_main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    test_main()