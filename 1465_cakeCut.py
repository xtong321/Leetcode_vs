"""
Cake Cutting Problem

**Problem**: Given rectangles (cakes) on a table, find where to make a horizontal cut so the total area above and below the cut line is equal.

**Approach**:
- Binary search on y-coordinate
- Calculate areas above/below cut line
- Handle partial rectangle intersections

test case: (x1, y1, x2, y2)
1) rect_list = [[0,0,10,10]], hcut = 5
2) rect_list = [[0,0,4,10], [6,0,12,10]], hcut = 5
3) rect_list = [[0,0,6,6], [6,2,12,8]], hcut = 4

idea:
1) find min_y and max_y as top and bottom
2) define mid = (top+bottom)/2
3) start from (top, bottom, mid) to compute top_area and bottom_area
4) if top_area is bigger, bottom = mid, and update mid, compute area; repeat till top_area = bot_area
"""

class Solution(object):
    def findCut(self, rect_list):
        """
        :type rect_list: a list of rects
        :rtype: int, horizontal cut line
        """
        if not rect_list:
            return -1

        N = len(rect_list) #[x1, y1, x2, y2]
        top = 100000
        bot = -1
        mid = 0
        tol_area = 0
        for i in range(N):
            the_rect = rect_list[i]
            top = min([top, the_rect[1], the_rect[3]])
            bot = max([bot, the_rect[1], the_rect[3]])
            tol_area += (the_rect[2]-the_rect[0])*(the_rect[3]-the_rect[1])

        print(f"top = {top}, bot = {bot}, tol_area = {tol_area}")
        top_area, bot_area = 1, 0
        loop = 0    
        while bot-top > 1:
            loop += 1        
            mid = int((top+bot)/2)
            top_area, bot_area = 0, 0
            # compute each rect area above mid_line
            for i in range(N):
                the_rect = rect_list[i]
                if the_rect[3] <= mid:
                    top_area += (the_rect[2]-the_rect[0])*(the_rect[3]-the_rect[1])
                elif the_rect[1] > mid:
                    top_area += 0
                else:
                    top_area += (the_rect[2]-the_rect[0])*(mid - the_rect[1])

            bot_area = tol_area - top_area
            print(f"loop: {loop}, top = {top}, bot = {bot}, mid = {mid}, top_area = {top_area}, bot_area = {bot_area}")

            if top_area > bot_area:
                bot = mid
            else:
                top = mid

            bot = int(bot)
            top = int(top)


        print(f"final ==> mid = {mid}, top_area = {top_area}, bot_area = {bot_area}\n")
        return mid


if __name__ == "__main__":
    #print(Solution().findCut([[0,0,10,10]])) # 5
    print(Solution().findCut([[0,0,4,10], [6,0,12,100]])) # 5
    #print(Solution().findCut([[0,0,6,6], [6,2,12,18]])) # 4
