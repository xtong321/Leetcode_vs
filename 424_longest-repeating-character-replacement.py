"""
424. 替换后的最长重复字符

给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
在执行上述操作后，返回 包含相同字母的最长子字符串的长度。

示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
可能存在其他的方法来得到同样的结果。
"""

class Solution:
    def characterReplacement(self, str_s, k):
        """
        Args:
          1) str_s (str): input str
          2) k (int): times that ch can change
        Return:
          1) int: length of max-repeating-char
        """
        if not str_s or k<0:
            return 0

        left = 0        
        max_count = 0
        max_len = 0
        count = {}
        for right in range(len(str_s)):
            ch = str_s[right]
            count[ch] = count.get(ch, 0)+1
            max_count = max(max_count, count[ch])
            if (right-left+1)-max_count > k:
                count[str_s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len


if __name__ == "__main__":
    # 输入：s = "ABAB", k = 2, 输出：4
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))

    # 输入：s = "AABABBA", k = 1, 输出：4
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))


