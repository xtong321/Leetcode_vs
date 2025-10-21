"""
描述：给定两个字符串 text1 和 text2。
要求：返回两个字符串的最长公共子序列的长度。如果不存在公共子序列，则返回 0。

说明：
子序列：原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
公共子序列：两个字符串所共同拥有的子序列。
1≤text1.length,text2.length≤1000。
text1 和 text2 仅由小写英文字符组成。

示例：
示例 1：
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
"""

class solution():
    def longestCommSubseq(self, text1, text2):
        if not text1 or not text2:
            return 0

        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2+1)] for _ in range(size1+1)]        
        ans = 0

        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                if ans < dp[i][j]:
                    ans = dp[i][j]

        return ans


if __name__ == "__main__":
    print(solution().longestCommSubseq("abcde", "ace")) # 3
    print(solution().longestCommSubseq("abc", "abc")) # 3
