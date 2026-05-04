"""
2542. Maximum Subsequence Score
You are given two 0-indexed integer arrays nums1 and nums2 of 
equal length n and a positive integer k. You must choose a 
subsequence of indices from nums1 of length k.
For chosen indices i0, i1, ..., ik - 1, your score is defined as:
The sum of the selected elements from nums1 multiplied with the 
minimum of the selected elements from nums2.
It can defined simply as: 
(nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.
A subsequence of indices of an array is a set that can be derived 
from the set {0, 1, ..., n-1} by deleting some or no elements.

Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
"""

from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)        
        # make nums1 and nums2 into a pair, and sort according to nums2 as descent
        #pairs = [(nums1[i], nums2[i]) for i in range(n)]
        #pairs.sort(key=lambda x: x[1], reverse=True)
        pairs = zip(nums1, nums2)
        sorted_pairs = sorted(pairs, key = lambda x:x[1], reverse = True)
        
        # use a min_healp to maintain nums1
        min_heap = []
        total = 0  # sum in nums1 with size = k
        max_score = 0

        # scan sorted pairs, select max(sum(num1, k) * min(num2, k))        
        for num1, num2 in sorted_pairs:
            # push num1 into heap
            heapq.heappush(min_heap, num1)
            total += num1
            if len(min_heap) > k:                
                total -= heapq.heappop(min_heap)
            
             # update the max-score
            if len(min_heap) == k:
                max_score = max(max_score, total * num2)

        return max_score

## test
if __name__ == "__main__":
    #test-1
    nums1 = [1,3,3,2]; nums2 = [2,1,3,4]; k = 3    #Output: 12
    print(f"test-1: GT = 12, predict = ", Solution().maxScore(nums1, nums2, k))

    #test-2 
    nums1 = [4,2,3,1,1]; nums2 = [7,5,10,9,6]; k = 1    #Output: 30
    print(f"test-2: GT = 30, predict = ", Solution().maxScore(nums1, nums2, k))

