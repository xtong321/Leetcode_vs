"""
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], 
determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true

Idea:
1) sort the meeting interval according to starting time
2) check if there is overlap between any two continuous meetings
3) if yes, return False (he cann't), otherwise return True (he can)
"""

class Solution(object):
    def func(self, meet_list):
        """
        :type meet_list: a list of meetings with [start, end]
        :rtype: True if he can, otherwise False if he cannot
        """
        if not meet_list:
            return True

        N = len(meet_list)
        meet_list.sort()

        for i in range(N-1):
            if meet_list[i+1][0] < meet_list[i][1]:
                return False
            
        return True

if __name__ == "__main__":
    print(Solution().func([[0,30],[5,10],[15,20]])) # False
    print(Solution().func([[7,10],[2,4]])) # True
