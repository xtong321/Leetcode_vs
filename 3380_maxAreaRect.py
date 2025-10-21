"""
You are given an array points where points[i] = [xi, yi] represents the coordinates of a point on an infinite plane.
Your task is to find the maximum area of a rectangle that:

Can be formed using four of these points as its corners.
Does not contain any other point inside or on its border.
Has its edges parallel to the axes.
Return the maximum area that you can obtain or -1 if no such rectangle is possible.

Example 1:
Input: points = [[1,1],[1,3],[3,1],[3,3]]
Output: 4

Idea:
1) sort these points according to one axis, say x value
2) repeat to find the vertical line, from right to left
3) scan from left to right till to the right line
4) check if it is a rect, if yes, compute the area, and save the max_area
5) return the max area and corresponding points
"""

class Solution(object):
    def maxRectArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        max_area = -1
        max_pts = []
        #pt_set = set(map(tuple(points))) # map for fast query
        pt_set = set(map(tuple, points))

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue                
                if (x1, y2) in pt_set and (x2, y1) in pt_set:
                    area = abs((x2-x1)*(y2-y1))
                    if max_area < area:
                        max_area = area
                        max_pts = [(x1, y1),(x2, y1), (x2, y2), (x1, y2)]

        if max_area < 0:
            return -1
        else:
            return max_area, max_pts


if __name__ == "__main__":
    print(Solution().maxRectArea([[2, 1], [-8, 1], [2, 4], [8, 4], [-8, -2], [2, -2]]))
