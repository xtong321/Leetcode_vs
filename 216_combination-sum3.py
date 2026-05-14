"""
216. Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain 
the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 
1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""

from typing import List

"""
我们设计一个函数 dfs(i, s), 表示当前枚举到数字 i, 还剩下和为 s 的数字需要枚举，当前搜索路径为 t, 答案为 ans 

函数 dfs(i, s)  的执行逻辑如下:
方式一：

如果 s=0, 且当前搜索路径 t 的长度为 k, 说明找到了一组答案，将 t  加入 
 ans 中，然后返回。

如果 i>9 或者 i>s, 或者当前搜索路径 t 的长度大于 k, 说明当前搜索路径不可能是答案，直接返回。

1) 否则，我们可以选择将数字 i 加入搜索路径 t 中，然后继续搜索，即执行 dfs(i+1,s-i)
搜索完成后，将 i 从搜索路径 t 中移除；我们也可以选择不将数字 i 加入搜索路径 t
中，直接执行 dfs(i+1, s)

2) 否则，我们枚举下一个数字 j, j in [i, 9], 将数字 j 加入搜索路径 t 中，
然后继续搜索，即执行 dfs(j+1, s-j), 搜索完成后，将 j 从搜索路径 t 中移除。
"""

class Solution:
    def combinationSum1(self, k: int, n: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                if len(t) == k:
                    ans.append(t[:])
                return
            if i > 9 or i > s or len(t) >= k:
                return
            t.append(i)
            dfs(i + 1, s - i)
            t.pop()
            dfs(i + 1, s)

        ans = []
        t = []
        dfs(1, n)
        return ans
    
    def combinationSum2(self, k: int, n: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                if len(t) == k:
                    ans.append(t[:])
                return
            if i > 9 or i > s or len(t) >= k:
                return
            for j in range(i, 10):
                t.append(j)
                dfs(j + 1, s - j)
                t.pop()

        ans = []
        t = []
        dfs(1, n)
        return ans
    

if __name__ == "__main__":
    k = 3; n = 7; Output = [[1,2,4]]
    print(Solution().combinationSum1(k, n))
    print(Solution().combinationSum2(k, n))