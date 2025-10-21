"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

#python2
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs)<=1:
            return " "

        for i in range(len(strs[0])):
            for str in strs:
                if len(str)<i or str[i] != strs[0][i]:
                    return strs[0][:i]
                
        return strs[0]

# python3
#class Solution:
#    def longestCommonPrefix(self, strs: List[str]) -> str:

if __name__ == "__main__":
    # strs = ["flower","flow","flight"]， Output: "fl"
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))

    # strs = ["dog","racecar","car"], Output: ""
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))