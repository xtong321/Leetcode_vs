"""
描述：给定两个单词 word1、word2。
对一个单词可以进行以下三种操作：
插入一个字符
删除一个字符
替换一个字符

要求：计算出将 word1 转换为 word2 所使用的最少操作数。

说明：
0≤word1.length,word2.length≤500。
word1 和 word2 由小写英文字母组成。

示例：
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
class solution():
    def editDist(self, word1, word2):
        size1 = len(word1)
        size2 = len(word2)

        dp = [[0 for _ in range(size2+1)] for _ in range(size1+1)]

        for i in range(1, size1+1):
            dp[i][0] = i
        for j in range(1, size2+1):
            dp[0][j] = j

        for i in range(1, size1+1):
            for j in range(1, size2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else: # replace, insert, delete, 
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[size1][size2]

if __name__ == "__main__":
    print(solution().editDist("", "fuck")) # 4
    print(solution().editDist("horse", "ros")) # 3
    print(solution().editDist("intention", "execution")) # 5
    
