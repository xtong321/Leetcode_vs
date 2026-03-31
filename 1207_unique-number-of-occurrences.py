"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Idea:
1) use a hasp_map to recorde the occurrance of each num
2) use a set to calculate the occurrance set
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}        
        for i, val in enumerate(arr):
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1
        # input val into a list        
        occu = list(freq.values())

        return True if len(set(occu))==len(occu) else False
    
    
    def func2(self, arr):
        # 1. 用字典统计频率
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # 2. 用集合检查唯一性
        seen = set()
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True



if __name__ == "__main__":
    arr = [1,2,2,1,1,3] # Output: true
    print(Solution().uniqueOccurrences(arr))

    arr = [1,2] # Output: false
    print(Solution().uniqueOccurrences(arr))

    arr = [-3,0,1,-3,1,1,1,-3,10,0] # Output: true
    print(Solution().uniqueOccurrences(arr))