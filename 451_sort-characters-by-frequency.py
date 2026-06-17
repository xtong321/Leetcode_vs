"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of 
the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        count = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(count.keys(), key=lambda c: count[c], reverse=True)
        
        # Build the output string
        return "".join(c * count[c] for c in sorted_chars)

    def frequencySort2(self, s: str) -> str:
        freq = {}
        for i, ch in enumerate(s):
            #freq[ch] += 1
            freq[ch] = freq.get(ch, 0) + 1

        # sort
        sorted_chars = sorted(freq.keys(), key=lambda c: freq[c], reverse=True)

        # joint and return
        return "".join(c * freq[c] for c in sorted_chars)


if __name__ == "__main__":
    s = "tree"; Output = "eert"
    print(f"input: {s};  sorted: ", Solution().frequencySort2(s))

    s = "Aabb"; Output = "bbAa"
    print(f"input: {s};  sorted: ", Solution().frequencySort2(s))
