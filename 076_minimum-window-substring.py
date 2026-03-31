"""
76. 最小覆盖子串
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，
使得该子串包含 t 中的每一个字符（包括重复字符）。
如果没有这样的子串，返回空字符串 ""。
"""

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)
        left, right = 0, 0
        formed = 0
        window_counts = {}
        min_len = float("inf")
        min_start = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                char_left = s[left]
                window_counts[char_left] -= 1
                if char_left in t_count and window_counts[char_left] < t_count[char_left]:
                    formed -= 1
                left += 1

            right += 1

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]

# Example usage:
if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABBC")) # Output: "BANC"