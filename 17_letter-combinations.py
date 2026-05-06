"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]
"""

from typing import List

hash_n_to_c = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [""]

        for n in digits:
            res = [x + y for x in res for y in hash_n_to_c[n]]

        return res
    

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output = []
        letter_map = {
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],''
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
            }
        if len(digits) ==0: 
            return []
        
        for key in digits:
            if key not in letter_map.keys():
                return [] #return[] if num is not in map
            
        def backtrack(combination, next_digits):
            if len(next_digits) == 0: #all nums are extracted if len =0
                output.append(combination)
            else:
                for letter in letter_map[next_digits[0]]: #select one char as char-connect
                    backtrack(combination + letter, next_digits[1:]) #next num

        backtrack("", digits)
        return output


if __name__ == "__main__":
    digits = "23"; Output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solution().letterCombinations(digits))

    digits = "2"; Output = ["a","b","c"]
    print(Solution().letterCombinations(digits))