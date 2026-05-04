"""
LeetCode 2336. Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet 
object to contain all positive integers.
int popSmallest() Removes and returns the smallest 
integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back
 into the infinite set, if it is not already in the infinite set.
"""

class SmallestInfiniteSet:

    def __init__(self):
        pass
        

    def popSmallest(self) -> int:
        pass
        

    def addBack(self, num: int) -> None:
        pass



# 使用 bisect
import bisect
class SmallestInfiniteSet2:
    def __init__(self):
        self.s = list(range(1, 1001))  # 1 到 1000 的有序列表

    def popSmallest(self) -> int:
        if not self.s:
            return -1  # 理论上不会空
        val = self.s[0]
        self.s.pop(0)  # 删除最小值
        return val

    def addBack(self, num: int) -> None:
        if num in self.s:
            return
        bisect.insort_left(self.s, num)  # 保持有序插入


"""
#使用 SortedSet 优化版本
from sortedcontainers import SortedSet
class SmallestInfiniteSet3:
    def __init__(self):
        self.s = SortedSet(range(1, 1001))

    def popSmallest(self) -> int:
        x = self.s[0]
        self.s.remove(x)
        return x

    def addBack(self, num: int) -> None:
        self.s.add(num)
"""


class SmallestInfiniteSet4:
    def __init__(self):
        self.nums = [False] * 1002  # 数组哈希
        self.small = 1

    def popSmallest(self) -> int:
        # 获取当前最小值
        x = self.small  # shadow copy?
        self.nums[x] = True
        # 更新最小值
        while self.nums[self.small]:
            self.small += 1
        return x

    def addBack(self, num: int) -> None:
        # 将 num 恢复为可用状态，并更新当前最小值
        self.nums[num] = False
        self.small = min(self.small, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
#Input
#["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
#[[], [2], [], [], [], [1], [], [], []]
#Output
#[null, null, 1, 2, 3, null, 1, 4, 5]
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

if __name__ == "__main__":
    obj = SmallestInfiniteSet4()
    #print(f"op-1: ", obj = SmallestInfiniteSet())
    print(f"op-2: ", obj.addBack(2))
    print(f"op-3: ", obj.popSmallest())
    print(f"op-4: ", obj.popSmallest())
    print(f"op-5: ", obj.popSmallest())
    print(f"op-6: ", obj.addBack(1))
    print(f"op-7: ", obj.popSmallest())
    print(f"op-8: ", obj.popSmallest())
    print(f"op-9: ", obj.popSmallest())
   