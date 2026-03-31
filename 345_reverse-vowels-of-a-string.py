"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Idea:
1) find all viwels, and record their index
2) reverse and get a LUT
3) replace each vowel in original list one by one

takeaway:
1) change str to list, ans = list(s)
2) change list to str, ans = "".join(list)
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        #vow_idx = [i if s[i] in 'aeiouAEIOU']
        vow_idx = []
        for i, ch in enumerate(s):
            if ch in 'aeiouAEIOU':
                vow_idx.append(i)

        #org_ch = s[vow_idx]
        org_ch = [ch for ch in s if ch in 'aeiouAEIOU']
        rev_ch = org_ch[:] #copy
        N = len(org_ch)
        if N<=0:
            return s

        for i in range(N):
            rev_ch[i] = org_ch[N-1-i]

        ans = list(s) # change str to a list
        j = 0 # in vow_index
        for i, ch in enumerate(s):
            if i in vow_idx: #ch in 'aeiouAEIOU'
                old = org_ch[j]
                new = rev_ch[j]
                ans[i] = new
                j += 1

        return "".join(ans)

    def func2(self, s: str) -> str:
        vowels = set("aeiouAEIOU") #define a set
        chars = list(s) #change str to list
        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)



if __name__ == "__main__":
    s = "IceCreAm"   #Output: "AceCreIm"
    print(f'{Solution().reverseVowels(s)}, expected_output = AceCreIm')

    s = "leetcode"   #Output: "leotcede"
    print(f'{Solution().reverseVowels(s)}, expected_output = leotcede')
