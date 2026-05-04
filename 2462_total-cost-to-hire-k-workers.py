"""
2462. Total Cost to Hire K Workers

You are given a 0-indexed integer array costs where costs[i] is 
the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to 
hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from 
either the first candidates workers or the last candidates workers. 
Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, 
then in the first hiring session, we will choose the 4th worker 
because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because 
they have the same lowest cost as 4th worker but they have the 
smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the 
worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

Example-1:
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11

Example-2:
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
"""

from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if not costs:
            return 0
        ans = 0
        max_cost = max(costs)   # initial cost

        # scan for each round
        k = min(k, len(costs))
        for i in range(k):
            # generate the candidate list
            min_cost = max_cost
            min_idx = 0
            # last candidates
            for j in range(len(costs)-candidates, len(costs)):
                if min_cost > costs[j]:
                    min_cost = costs[j]
                    min_idx = j
            # first candidates, prefer cost in the first candidates
            for j in range(0, j):
                if min_cost >= costs[j]:
                    min_cost = costs[j]
                    min_idx = j

            # select the best candidate

            # update the remain worker list            
            removed_element = costs.pop(min_idx)
            #del costs[min_idx]

            # next round
            ans += min_cost

        return ans

## test
# Example-1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11

# Example-2:
# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
if __name__ == "__main__":
    # test-1:
    costs = [17,12,10,2,7,2,11,20,8]; k = 3; candidates = 4
    GT_output = 11
    print(f"test-1: GT_out={GT_output}, pred_out = ", Solution().totalCost(costs, k, candidates))


    costs = [1,2,4,1]; k = 3; candidates = 3
    GT_output = 4
    print(f"test-1: GT_out={GT_output}, pred_out = ", Solution().totalCost(costs, k, candidates))
