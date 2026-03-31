"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Idea:
1) calculate distance from every point to Origin
2) note a data structure [[xi, yi, di]]
3) sort online for the third dim, or just use the distance to rank, and keep the ordered index
"""
import heapq
from typing import List

class Solution(object):
    def kClosest_1(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not points or k<=0:
            return None

        N = len(points)
        if k >= N:
            return points

        # calculate distance for every point
        dists = [0 for _ in range(N)]
        for i in range(N):
            x = points[i][0]
            y = points[i][1]
            dist = x*x + y*y
            dists[i] = dist

        # sort
        #index = sorted(dists)
        '''
        >>> x[np.argsort(x)] #通过索引值排序后的数组
        array([1, 2, 3])
        >>> x[np.argsort(-x)]
        array([3, 2, 1])
        '''     
        sorted_indices = [i for i, _ in sorted(enumerate(dists), key=lambda x: x[1])]
        #print(sorted_indices)  # 输出: [3, 1, 2, 0]        
        k_pts = []
        for i in range(k):
            index = sorted_indices.index(i)
            k_pts.append(points[index])

        return k_pts


    def kClosest_2(self, points, k):
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]

    def kClosest_3(self, points, K):
        a = lambda x :x[0]**2 + x[1]**2
        points.sort(key = a) # the input points data has been changed
        return points[:K]

    
    def kClosest_heap(self, points, k):
        if k >= len(points):
            return points
        # max-heap emulated by storing (-dist, x, y) or store (dist, point) and use min-heap of size k with neg dist
        heap = []
        for x, y in points:
            dist = x*x + y*y
            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y))   # keep k smallest -> store negative to emulate max heap
            else:
                if -heap[0][0] > dist:  # current farthest in heap farther than new point
                    heapq.heapreplace(heap, (-dist, x, y))

        #heap.reverse(), or return [[x, y] for (_, x, y) in heap[::-1]]
        return [[x, y] for (_, x, y) in heap]

    def kClosest(self, points, k):
        max_q = []
        for i, (x, y) in enumerate(points):
            dist = x*x + y*y #math.hypot(x, y)
            heapq.heappush(max_q, (-dist, i))
            if len(max_q) > k:
                heapq.heappop(max_q)
        return [points[i] for _, i in max_q]

if __name__ == "__main__":
    #print(Solution().kClosest_1(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3,3],[-2,4]]
    #print(Solution().kClosest_1(points = [[1,3],[-2,2]], k = 1)) # [[-2,2]]
    print(Solution().kClosest_heap(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3,3],[-2,4]]
    print(Solution().kClosest_heap(points = [[1,3],[-2,2]], k = 1)) # [[-2,2]]
    
        
