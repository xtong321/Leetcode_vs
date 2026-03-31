"""
2390. Removing Stars From a String
ref: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
You are given a string s, which contains stars *.

In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
- Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 
Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""
## idea:
# 1) find count of star
# 2) repeat until all stars are removed
#    2.1) scan to get the first star
#    2.2) remove the char and the star
#    2.3) repeat

from collections import Counter

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        str = s[:] # copy, or direct =
        size = len(str)
        count = str.count('*')
        if count<=0:
            return s
        
        
        iterations = 0
        while count > 0 and iterations <= size:
            for i, ch in enumerate(s):
                if ch == '*':
                    if i>0:
                        str = s.replace(s[i-1:i+1], '', 2)
                    else:
                        str = s.replace(s[i-1], '', 1)
                    s = str
                    break
                
            count -= 1

        return s


if __name__ == "__main__":
    s = "leet**cod*e" # Output: "lecoe"
    #print(Solution().removeStars(s))

    s = "erase*****" # Output: ""
    print(Solution().removeStars(s))