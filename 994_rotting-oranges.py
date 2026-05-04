"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent 
to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until 
no cell has a fresh orange. If this is impossible, return -1.

Example-1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example-2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example-3:
Input: grid = [[0,2]]
Output: 0
"""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        # BFS to spread the rot
        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes if fresh_count == 0 else -1

if __name__ == "__main__":
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # Output: 4
    print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # Output: -1
    print(Solution().orangesRotting([[0,2]])) # Output: 0
        