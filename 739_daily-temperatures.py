"""
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there is no future day 
for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        if not temps:
            return None
        ans = []
        curr = 0; next = 0
        N = len(temps)
        for i in range(N-1):
            wait = 0
            for j in range(i+1, N):
                if temps[j] > temps[i]:
                    wait = j - i
                    break
            ans.append(wait)

        ans.append(0) # last item
        return ans

if __name__ == "__main__":
    temps = [73,74,75,71,69,72,76,73]; Output = [1,1,4,2,1,1,0,0]
    print(Solution().dailyTemperatures(temps))

    temps = [30,40,50,60]; Output = [1,1,1,0]
    print(Solution().dailyTemperatures(temps))

    temps = [30,60,90]; Output = [1,1,0]
    print(Solution().dailyTemperatures(temps))
