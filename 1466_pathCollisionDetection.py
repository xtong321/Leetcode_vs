"""
Waymo interview
### 5. Path Collision Detection

**Problem**: Given circular obstacles in a region, determine if a vehicle can traverse from bottom to top.

**Requirements**:
- Vehicle can take any path (not necessarily straight)
- Merge overlapping circles
- Check if merged obstacles block entire width

**Algorithm**:
1. Merge overlapping circles into larger regions
2. Sort obstacles by x-coordinate
3. Check if any obstacle group spans entire width
"""

import math

class Circle:
    def __init__(self, cx=0, cy=0, radius=0, visited=False):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.visited = visited # it is visited o not

class Cluster:
    def __init__(self, idx_list=[]):
        self.idx_list = idx_list

class Solution(object):
    def pathCollision(self, rect, circles):
        """
        :type rect: [x1,y1,x2,y2]
        :type circle_list: list of circles
        :rtype bool: True if it is blocked, or False it not blocked
        :idea:
          1) merge circles into connected clusters
          2) check each cluster, if its connected centers block horizontal line
        """

        N = len(circles)
        print(f'circle_cnt = {N}')

        circle_list = []
        cluster_list = [] # clustered circle, merge connected circle
        for i in range(len(circles)):
            the_circle = Circle(circles[i][0],circles[i][1],circles[i][2],False)
            circle_list.append(the_circle)

        print(f'circle_list_cnt = {len(circle_list)}')
        
        h_block = False # block flag = False
        
        if N==1:
            if circle_list[0].cx-circle_list[0].radius <= rect[0] and\
            circle_list[0].cx+circle_list[0].radius >= rect[2]:
                h_block = True
                return h_block
        
        # generate N cluster        
        for i in range(N):
            the_cluster = Cluster([])
            the_cluster.idx_list.append(i)
            cluster_list.append(the_cluster)

        print(f'cluster_cnt = {len(cluster_list)}')
        
        for i in range(N-1):            
            # check if there is connected circle
            for j in range(i+1, N):
                if math.sqrt((circle_list[i].cx-circle_list[j].cx)*(circle_list[i].cx-circle_list[j].cx)+\
                (circle_list[i].cy-circle_list[j].cy)*(circle_list[i].cy-circle_list[j].cy)) <= (circle_list[i].radius + circle_list[j].radius):
                    # merge j into i, and remove j
                    cluster_list[i].idx_list.append(j)
                    cluster_list[j].idx_list = []

        # count how many valid cluster
        valid_cluster_cnt = 0
        for i in range(N):
            if len(cluster_list[i].idx_list) >= 1:
                valid_cluster_cnt += 1

        print(f'valid_cluster_cnt = {valid_cluster_cnt}')        
        for i in range(N):
            if len(cluster_list[i].idx_list) < 1:
                continue
            # process for cluster
            min_x = 10000
            max_x = -1
            for j in range(len(cluster_list[i].idx_list)):
                circle_idx = cluster_list[i].idx_list[j]
                min_x = min([min_x, circle_list[circle_idx].cx - circle_list[circle_idx].radius])
                max_x = max([max_x, circle_list[circle_idx].cx + circle_list[circle_idx].radius])

            if min_x <= rect[0] and max_x >= rect[2]:
                h_block = True
                return h_block
        
        return h_block

if __name__ == "__main__":
    print(Solution().pathCollision([0,0,100,50], [[20,20,30],[80,20,40]]))



