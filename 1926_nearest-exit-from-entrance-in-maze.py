"""
1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
and walls (represented as '+'). You are also given the entrance of the maze, 
where entrance = [entrancerow, entrancecol] denotes the row and column of the 
cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into 
a cell with a wall, and you cannot step outside the maze. Your goal is to find the 
nearest exit from the entrance. An exit is defined as an empty cell that is at the 
border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, 
or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

"""

from typing import List
from collections import deque

class Solution:    
    def nearestExit2(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # directions, right, left, down, up
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1])])  # deque to store coordinate
        maze[entrance[0]][entrance[1]] = '+'  # a list to record the visited grid
        step = 0  # number of steps
        
        while queue:
            step += 1
            size = len(queue)
            
            for _ in range(size):
                x, y = queue.popleft()
                
                # scan 4 directions
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    # check if new coordinates are valid
                    if 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == '.':
                        # if reach boundary, return
                        if new_x == 0 or new_x == m - 1 or new_y == 0 or new_y == n - 1:
                            return step
                        
                        # otherwise, continue to move
                        queue.append((new_x, new_y))
                        maze[new_x][new_y] == '+'
        
        # if do not find exit, return -1
        return -1
    

if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]; entrance = [1,2]
    #Output: 1
    print(f"test-1: ", Solution().nearestExit2(maze, entrance))


    maze = [["+","+","+"],[".",".","."],["+","+","+"]]; entrance = [1,0]
    #Output: 2
    print(f"test-2: ", Solution().nearestExit2(maze, entrance))


    maze = [[".","+"]]; entrance = [0,0]
    #Output: -1
    print(f"test-3: ", Solution().nearestExit2(maze, entrance))