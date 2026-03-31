"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Idea:
1) find #0 <= n+1, return false
2) scan this array, if there is continuous three 0, fill 1 in the middle plance, record the pointer
3) update this array, and continute to scan from this pointer
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed:
            return False
        if n<=0:
            return True

        N = len(flowerbed)
        count_1 = sum(flowerbed)
        count_0 = N - count_1

        if count_0 <= n+1:
            return False

        bed = flowerbed
        i = 0
        for i in range(0, N):
            if bed[i] > 0:
                continue

            left = max(0, i-1)
            right = min(N-1, i+1)
            # fill 1 if left and right are 0
            if bed[left] + bed[right] == 0:
                bed[i] = 1
            
        new_count_1 = sum(bed)

        if new_count_1 - count_1 >= n:
            return True
        else:
            return False

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    #Output: true
    print(Solution().canPlaceFlowers(flowerbed, n))

    flowerbed = [1,0,0,0,1]
    n = 2
    #Output: false
    print(Solution().canPlaceFlowers(flowerbed, n))

    
