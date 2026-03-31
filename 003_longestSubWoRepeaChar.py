"""
longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, in_str):
        """
        :type in_str: input str
        :rtype: int, size of longest substring w/o repeat characters
        """
        if not in_str:
            return 0
        if len(in_str)<=1:
            return len(in_str)

        max_size = 0
        size = 0
        left = 0 # start pointer
        idx = 0 # moving pointer
        hashmap = {}
        for idx, ch in enumerate(in_str):
            if ch in hashmap:
                size = idx - left
                max_size = max(max_size, size)
                left = max(left, hashmap[ch] + 1)
                # reset hashmap
                hashmap.pop(ch, None) # or del hashmap[ch]
            hashmap[ch] = idx     
            size = idx - left + 1
            max_size = max(max_size, size)
        return max_size

    def lengthOfLongestSubstring2(self, s: str) -> int:
       ans = left = 0
       window = {}
       for right, c in enumerate(s):
           if c in window:
               left = max(window[c] + 1, left)
           window[c] = right
           ans = max(ans, right - left + 1)
       return ans

if __name__ == "__main__":
    # Input: s = "abcabcbb", Output: 3
    # Input: s = "bbbbb", Output: 1
    # Input: s = "pwwkewt", Output: 4
    in_str1 = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(in_str1))

    in_str2 = "bbbbb"
    print(Solution().lengthOfLongestSubstring(in_str2))

    in_str3 = "pwwkewt"
    print(Solution().lengthOfLongestSubstring(in_str3))
