"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Idea:
1) generate a looku table between roman and int
2) divide a roman str into separate roman and transfer each of them into int
3) sum up all
Value   Roman numeral
1000 M
900 CM
500 D
400 CD
100 C
90 XC
50 L
40 XL
10 X
9 IX
5 V
4 IV
1 I
"""

class Solution(object):
    def roman2int(self, roman):
        #char = ['M', 'CM', 'D', 'CD', 'C','XC','L','XL','X','IX','V','IV','I']
        #nums = [1000, 900, 500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
        roman_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        str = roman
        ans = 0

        #for i, ch in enumerate(roman):
        i = 0
        while i < len(roman):
            if roman[i:i+2] in roman_dict.keys():
                #idx = ...
                #ans += nums[idx]
                #roman.remove(i:i+2) # remove the char at [idx_i -> i+1]
                ans += roman_dict[roman[i:i+2]]
                #roman.remove(i) # remove the char at idx_i, .pop(idx)
                #roman.remove(i+1) # remove the char at idx_i
                i+=2
            elif roman[i] in roman_dict.keys():                
                ans += roman_dict[roman[i]]
                #roman.remove(i) # remove the char at idx_i, .pop(idx)
                i+=1
            
        return ans


if __name__ == "__main__":
    s = "III" #Output: 3
    print(Solution().roman2int(s))

    s = "LVIII" #Output: 58
    print(Solution().roman2int(s))

    s = "MCMXCIV" #Output: 1994
    print(Solution().roman2int(s))

