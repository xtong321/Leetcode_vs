"""
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

题目回顾
给定两个字符串 word1 和 word2。

操作规则：
- 交换任意两个字符（相当于打乱顺序）。
- 交换两种字符的所有出现次数（比如把所有 a 换成 b，同时把所有 b 换成 a）。

问：能否通过若干次操作把 word1 变成 word2。

核心条件
- 字符集合必须相同, 
  因为操作不会引入新字符，也不会删除已有字符。
  所以 set(word1) == set(word2)。
- 字符频率分布必须相同（排序后）
  操作 2 可以交换字符的频率，但不能改变频率集合。
  所以只要两个字符串的频率多集合相同，就能通过交换得到。

解法步骤
- 如果长度不同 → 返回 False。
- 统计两个字符串的字符频率。
- 比较字符集合是否相同。
- 比较频率分布排序后是否相同。
- 满足条件 → 返回 True，否则 False。
"""

from collections import Counter

class Solution:
    def func1(self, word1: str, word2: str) -> bool:
        # 长度不同直接返回 False
        if len(word1) != len(word2):
            return False
        
        # 统计频率
        c1, c2 = Counter(word1), Counter(word2)
        
        # 条件 1: 字符集合相同
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        # 条件 2: 频率分布相同
        return sorted(c1.values()) == sorted(c2.values())

    def func2(self, word1: str, word2: str) -> bool:
        # 长度不同直接返回 False
        if len(word1) != len(word2):
            return False
        
        # 统计频率
        c1, c2 = {}, {} #Counter(word1), Counter(word2)
        for i, ch in enumerate(word1):
            if ch in c1:
                c1[ch] += 1
            else:
                c1[ch] = 1
        for i, ch in enumerate(word2):
            if ch in c2:
                c2[ch] += 1
            else:
                c2[ch] = 1
        
        # 条件 1: 字符集合相同
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        # 条件 2: 频率分布相同,排序后的 historgram 相同
        return sorted(c1.values()) == sorted(c2.values())


if __name__ == "__main__":
    word1, word2 = "abc", "bca" # Output: true
    print(Solution().func2(word1, word2))

    word1, word2 =  "a", "aa" # Output: false
    print(Solution().func2(word1, word2))

    word1, word2 = "cabbba", "abbccc" # Output: true
    print(Solution().func2(word1, word2))