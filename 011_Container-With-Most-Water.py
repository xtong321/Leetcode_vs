"""
Container With Most Water
给定一组长短不一的隔板，挑其中的两块板，使得板子之间能装最多的水。
注意点：
两块板之间能装多少水是由短的那块板决定的
选定两块板之后，它们之间的板就不存在了
例子：
输入: height=[1,1,1] 输出: 2
解题
"""
class Solution(object):
    def maxArea(self, height_list):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height_list:
            return 0

        left = 0
        right = len(height_list)-1
        # final result
        result = 0
        opt_left = left
        opt_right = right

        while left < right:
            if height_list[left] < height_list[right]:
                area = height_list[left] * (right - left)
                if area > result:
                    opt_left = left
                    opt_right = right
                result = max(result, area)
                left += 1
            else:
                area = height_list[right] * (right - left)
                if area > result:
                    opt_left = left
                    opt_right = right
                result = max(result, area)
                right -= 1
        
        return result, opt_left, opt_right


if __name__ == "__main__":
    print(Solution().maxArea([1, 1, 2]))
    print(Solution().maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
