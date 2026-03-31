"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of 
vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Idea:
1) sliding window to count
"""

class Solution(object):
    def maxVowels(self, str, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not str or k<=0:
            return 0
        if len(str) < k:
            return 0

        N = len(str)
        str = str.lower()

        start, end, win_cnt = 0, 0, 0
        opt_start, opt_end, opt_cnt = 0, 0, 0

        #initial value
        start = 0 # included
        end = start + k  # not included
        for i in range(start, end):
            if str[i] in "aeiou":
                win_cnt += 1
        
        opt_start = start
        opt_end = end
        opt_cnt = win_cnt
        for start in range(1, N-k):
            end = start + k - 1
            if str[end] in "aeiou":
                win_cnt += 1
            if str[start-1] in "aeiou":
                win_cnt -= 1
            
            if opt_cnt < win_cnt:
                opt_cnt = win_cnt
                opt_start = start
                opt_end = end

        return [opt_start, opt_end, opt_cnt]


if __name__ == "__main__":
    s, k = "abciiidef", 3 # Output: 3
    print(Solution().maxVowels(s, k))

    s,k = "aeiou", 2 # Output: 2
    print(Solution().maxVowels(s, k))

    s, k = "leetcode", 3 # Output: 2
    print(Solution().maxVowels(s, k))
            