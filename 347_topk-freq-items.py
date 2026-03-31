"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""

from collections import Counter

class Solution(object):
    def top_k_frequent(self, nums, k):
        """
        :type nums: input number list
        :type k: top-k
        """
        if not nums:
            return None
        
        # count
        freq_map = Counter(nums)
        # sorted by (freq, num)
        sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], -x[0]))
        #extract sorted top-k
        return [item[0] for item in sorted_items[:k]]


# test
if __name__ == "__main__":
    nums = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    # print(top_k_frequent(nums, k)) # Output: [4, 1]
    print(Solution().top_k_frequent(nums, k))
