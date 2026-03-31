"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

示例 3：
输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。 
"""

class Solution(object):
    #def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge1(self, intervals):
        """
        :type intervals: List[List[int]]
        "rtype: merged intervals, List[List[int]]
        """
        if not intervals:
            return None

        # sort accorinding to the start_i
        N = len(intervals)
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # merge one-by-one
        """
        res = []
        res.append(sorted_intervals[0])
        for k in range(1, N):
            if sorted_intervals[k][0] <= res[-1][1]:
                res[-1][1] = max(sorted_intervals[k][1], res[-1][1])
            else:
                res.append(sorted_intervals[k])
        """

        i = 0
        j = 1
        while i < len(sorted_intervals)-1:
            box_i = sorted_intervals[i]
            while j < len(sorted_intervals):
                box_j = sorted_intervals[j]
                if box_i[1] >= box_j[0]:
                    box_i[1] = box_j[1]
                    sorted_intervals.pop(j)
                else:
                    j += 1
            i += 1
        res = sorted_intervals
        """
        for i in range(len(sorted_intervals)-1):
            box_i = sorted_intervals[i]
            for j in range(i+1, len(sorted_intervals)):
                box_j = sorted_intervals[j]
                if box_i[1] >= box_j[0]:
                    box_i[1] = box_j[1]
                    sorted_intervals.pop(j)
                    j = j-1
        """    
        return res


    def merge2(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res

# test
if __name__ == "__main__":
    intervals = [[4,7],[1,4]] # out: [[1,7]]
    print(Solution().merge1(intervals))

    intervals = [[1,3],[2,6],[8,10],[15,18]] # out: [[1,6],[8,10],[15,18]]
    print(Solution().merge1(intervals))
        
