"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Idea:
1) split the string into list of words, and remove abundent blank
2) reverse the list of words to generate a new list
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None

        print(f'=> original string: {s}')

        # str to list
        #word_list = s.split(" ") # extract word, reserve space
        word_list = s.split() # retrieve words seperate by space
        # remove redundent space ??
        print(f'=> original words: {word_list}')

        new_list = word_list[::-1]
        new_str = " ".join(new_list)
        """N = len(word_list)
        for i in range(N-1, -1, -1):
            word = word_list[i]
            new_list.append(word)
            if i != 0:
                new_list.append(' ')
        
        new_str = ''
        new_str = ",".join(map(new_list))
        return new_str
        """
        return new_str


if __name__ == "__main__":
    s = "the sky is blue" # Output: "blue is sky the"
    print(Solution().reverseWords(s) + '\n')

    s = "  hello world  "  # Output: "world hello"
    print(Solution().reverseWords(s) + '\n')

    s = "a good   example"  # Output: "example good a"
    print(f'{Solution().reverseWords(s)}\n')