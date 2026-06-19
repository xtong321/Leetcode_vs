"""
1268. Search Suggestions System
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products
 after each character of searchWord is typed. Suggested products should 
 have common prefix with searchWord. If there are more than three products 
 with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
"""

from typing import List

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.n = 0
        self.words = list()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode

            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return ""
            node = node.children[char]
        return node.words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ret = []
        word = ""
        products.sort()
        for i in range(len(searchWord)):
            tmp = []
            word += searchWord[i]
            for product in products:
                if product[:i+1] == word and len(tmp) < 3:
                    tmp.append(product) 
            ret.append(tmp)

        return ret
    

    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = list()
        products.sort()
        for i in range(1, len(searchWord)+1):
            products = list(filter(lambda x: x.startswith(searchWord[:1]), products))
            res.append(products[:3])

        return res
    
    def suggestedProducts3(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.insert(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            ans.append(trie.search(cur))
            
        return ans
    


  
if __name__ == "__main__":
    products = ["mobile","mouse","moneypot","monitor","mousepad"]; searchWord = "mouse"
    #Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
    print(Solution().suggestedProducts(products, searchWord))