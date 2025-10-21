"""
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], 
return the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1

Idea: it is like the IOU calculation
1) sort all meeting_list
2) check overlaped meetings, and tag the flag of verlap
3) check each overlapped meeting, how many meetings the end time is within
"""

class Meeting(object):
    def __init__(self, start, end, overlap = False):
        self.start = start
        self.end = end
        self.overlap = overlap

class Solution(object):
    def func(self, meet_list):
        """
        :type meet_list: a list of meetings with [start, end]
        :rtype: True if he can, otherwise False if he cannot
        """
        if not meet_list:
            return True

        N = len(meet_list)
        old_meet_list = []
        #generate a list
        for i in range(N):
            one_meet = Meeting(meet_list[i][0], meet_list[i][1], False)
            old_meet_list.append(one_meet)

        sorted_meet_list = sorted(old_meet_list, key=lambda Meeting: Meeting.start)
        #meet_list.sort()

        for i in range(N-1):
            if sorted_meet_list[i+1].start < sorted_meet_list[i].end:
                sorted_meet_list[i].overlap = True
                sorted_meet_list[i+1].overlap = True
                
        #check each end of overlapped meeting
        max_overlap_cnt = 0
        for i in range(N):
            if sorted_meet_list[i].overlap == False:
                continue

            the_end = sorted_meet_list[i].end
            overlap_cnt = 0
            for k in range(N):
                if the_end > sorted_meet_list[k].start and the_end <= sorted_meet_list[k].end:
                    overlap_cnt += 1

            max_overlap_cnt = max([max_overlap_cnt, overlap_cnt])
        
        return max_overlap_cnt if max_overlap_cnt > 0 else 1

if __name__ == "__main__":
    print(Solution().func([[0,30],[5,10],[15,20]])) # 2
    print(Solution().func([[7,10],[2,4]])) # 1
    print(Solution().func([[0,30],[5,10],[15,20], [1, 40], [35,38]])) # 3