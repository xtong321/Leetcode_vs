"""
longest-palindromic-substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

class Solution(object):
    def func1(self, in_str):
        """
        :type s: str
        :rtype: str
        :Idea:
           1) find a repeated ch
           2) decide start and end
           3) check if it is palindromic between them
        """
        if not in_str:
            return 0

        # define 2 pointers from left and right
        left = 0
        rigth = 0
        record = [[] for i in range(0, 256)] # [ch] = index
        for i, ch in enumerate(in_str):
            record[ord(ch)].append(i)

        # check if there is repeated ch
        max_size = 0
        max_str = []
        for i in range(len(record)):
            if len(record[i]) <= 1:
                continue
            for j in range(len(record[i])-1):
                for k in range(j+1, len(record[i])):
                    left  = record[i][j]
                    right = record[i][k]
                    ans = self.is_palindromic(in_str, left, right)
                    if ans:
                        max_size = max(max_size, right-left+1)
                        max_str = in_str[left:right+1]
        
        return max_str

    def is_palindromic(self, in_str, left, right):
        ans = False
        N = right - left + 1       
        while left <= right:
            if in_str[left] == in_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = "babad" #Output: "bab"
    print(Solution().func1(s))

    s = "cbbd" #Output: "bb"
    print(Solution().func1(s))
