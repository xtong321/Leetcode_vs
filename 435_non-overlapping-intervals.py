"""
435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. 
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #pass
        """
        idea:
        1) sort the intervals according ending time
        2) loop1: scan for each interval i for [i, end-1]
        3) loop2: scan each interval from [i+1, end]
           if there is overlap, remove the second one, and update interval list
           otherwise, continue           
        """
        if not intervals:
            return 0
        N = len(intervals)
        intervals.sort(key=lambda x: x[1]) # sort by end        
        prevEnd = float('-inf') # set a minimum data initially
        result = 0 # number of items to be removed
        ans = [] # recorde the items that will be removed
        for start, end in intervals:
            if prevEnd > start:
                #print(prevEnd, start, end)
                result += 1
                ans.append([start, end])
            else:
                prevEnd = end
        return result, ans


## test
if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [2, 7]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1, 2], [1, 2], [1, 2]]
    print(Solution().eraseOverlapIntervals(intervals))
    
    intervals = [[1, 2], [2, 3]]
    print(Solution().eraseOverlapIntervals(intervals))
