"""
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

Idea:
1) rank all the words by character, and generate a dick containing old word and new word
2) scan the ranked words, if not in a list, push it to the list
3) return the final list
"""

class Solution:
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        N = len(strs)
        # 1) sorting
        sorted_strs = list(strs)
        for i in range(0, N):
            str = sorted_strs[i]
            new_str = "".join(sorted(str))
            sorted_strs[i] = new_str
 
        new_strs = sorted_strs #tuple(sorted_strs)

        # 2) generate non-duplicated words
        res = []
        word_map = {}
        index = 0
        for i in range(0, N):
            new_str = new_strs[i]
            if new_str in word_map:
                index = word_map[new_str]
                res[index].append(strs[i])
            else:
                word_map[new_str] = index
                one_str = []
                one_str.append(strs[i])
                res.append(one_str)
                index += 1

        # 3) return the final list
        return res

    def groupAnagrams2(self, strs):
        """
        : type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for i, v in enumerate(strs):
            target = "".join(sorted(v)) # a joint character to a word
            #target = sorted(v) # a list of every character
            if target not in map:
                map[target] = [v]
            else:
                map[target].append(v)

        result = []
        for value in map.values():            
            result += [sorted(value)]

        return result
        

if __name__ == "__main__":
    print(Solution().groupAnagrams2(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams(strs = ["a"]))
    print(Solution().groupAnagrams(strs = [""]))
        