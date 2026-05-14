"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        idea: DP
        dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i], dp[i-1])
        """
        if not cost or len(cost)==1:
            return 0        
        N = len(cost)
        if N==2:
            return min(cost[0], cost[1])
                
        dp = [0 for _ in range(N+2)]

        for i in range(N-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])
    
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        """
        idea: DP
        dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i], dp[i-1])
        """
        if not cost or len(cost)==1:
            return 0        
        N = len(cost)
        if N==2:
            return min(cost[0], cost[1])
        
        # dp[i] = min_cost when reach stage_i
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        dp = [0 for _ in range(N+2)]
        for i in range(2, N+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[N]

        """dpa = dpb = 0
        for i in range(2, N+1):
            old_dpb = dpb
            dpb = min(dpb + cost[i-1], dpa + cost[i-2])
            dpa = old_dpb
        return dpb
        """


if __name__ == "__main__":
    cost = [10,15,20]; Output = 15
    print(f"test-1: ans = {Output}, pred = ", Solution().minCostClimbingStairs2(cost))

    cost = [1,100,1,1,1,100,1,1,100,1]; Output = 6
    print(f"test-1: ans = {Output}, pred = ", Solution().minCostClimbingStairs2(cost))