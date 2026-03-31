"""
1768: merge-strings-alternately

We are given two strings word1 and word2.
Our task is to merge the strings by adding letters in alternating order, 
starting with word1. If one string is longer than the other, 
the additional letters must be appended to the end of the merged string.

We must return the merged string that has been formed.
"""

class Solution(object):
    def func1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1 and not word2:
            return None
        if not word1 and word2:
            return word2
        if word1 and not word2:
            return word1

        N1 = len(word1)
        N2 = len(word2)
        i = 0
        j = 0
        new_word = ''
        while i<N1 and j<N2:
            new_word += word1[i]
            i += 1
            new_word += word2[j]
            j += 1

        if i<N1:
            new_word += word1[i:]
        if j<N2:
            new_word += word2[j:]

        return new_word

if __name__ == "__main__":
    word1 = 'abc'
    word2 = 'defg'
    print(Solution().func1(word1, word2)) # 'adbecfg'

    word1 = 'abcxy'
    word2 = 'def'
    print(Solution().func1(word1, word2)) # 'adbecfxy'

