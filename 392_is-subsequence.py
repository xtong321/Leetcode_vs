"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, 
or false otherwise.
A subsequence of a string is a new string that is formed from 
the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Idea:
1) generate a 2-D array to record ch-ch matching matrix
2) scan rows, to find the first matching
3) if following matching 1 whose col is bigger than before, till to end of str_s, return True
"""

class Solution(object):
    def func1(self, str_s, str_t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not str_s or not str_t:
            return False
        M = len(str_s)
        N = len(str_t)
        if M>N:
            return False

        # find the first row for the first match
        count = 0
        for i in range(M):            
            for j in range(i, N):
                if str_s[i] == str_t[j]:
                    count += 1
                    break
        
        if count == len(str_s):
            return True
        else:
            return False

    def func2(self, str_s, str_t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not str_s or not str_t:
            return False
        M = len(str_s)
        N = len(str_t)
        if M>N:
            return False

        DP = [[0 for _ in range(N)] for _ in range(M)]
 
        # find the first row for the first match        
        i, j = 0, 0
        while i < M and j < N:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == "__main__":
    s, t = "abc", "ahbgdc" # Output: true
    print(Solution().func1(s, t))

    s, t = "axc", "ahbgdc" # Output: false
    print(Solution().func1(s, t))
        