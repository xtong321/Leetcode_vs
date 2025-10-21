"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入：heights = [2,1,5,6,2,3]
输出：10
"""

class Solution(object):
    def largestRectArea(self, heights):
        area = 0
        for i in range(len(heights)):
            left = i-1
            right = i+1
            w = 1
            while left>=0:
                if heights[left] > heights[i]:
                    w+=1
                    left -= 1
                else:
                    break
            while right<=len(heights)-1:
                if heights[right] > heights[i]:
                    w+=1
                    right += 1
                else:
                    break
            area = max(area, w*heights[i])

        return area


if __name__ == "__main__":
    print(Solution().largestRectArea([2,1,5,6,2,3]))
        