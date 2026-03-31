"""
841. Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms 
are locked except for room 0. Your goal is to visit all the rooms. 
However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, 
and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that 
you can obtain if you visited room i, return true if you can 
visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only
 key that unlocks it is in that room.
"""
from typing import List
from collections import deque

class Solution(object):
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])

        while queue:
            current_room = queue.popleft()
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)

    def canVisitAllRooms8(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        def dfs(self, room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        visited = set()
        dfs(0)
        return len(visited)==len(rooms)
                

#test
if __name__ == "__main__":
    sol = Solution()
    # ex-1
    #Input: rooms = [[1],[2],[3],[]]
    #Output: true
    print("=> test-1: ")    
    rooms = [[1],[2],[3],[]]
    print(rooms)
    print(sol.canVisitAllRooms1(rooms))
    print(sol.canVisitAllRooms2(rooms))

    # ex-2
    # Input: rooms = [[1,3],[3,0,1],[2],[0]]
    # Output: false
    print("=> test-2: ")
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(rooms)
    print(sol.canVisitAllRooms1(rooms))
    print(sol.canVisitAllRooms2(rooms))