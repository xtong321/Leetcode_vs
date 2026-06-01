"""
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price 
of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        greddy algo
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        ans = 0
        for i in range(1, len(prices)):
            ans += (max(prices[i]-prices[i-1], 0))

        return ans

    def maxProfit2(self, prices):
        """
        DP        
        """
        if not prices:
            return 0

        # init states 1)non_holding, and 2) holding stocks
        dp0 = 0; dp1 = -prices[0]
        N = len(prices)
        for i in range(1, N):
            # non_holding currently: non_holding last time / holding and sell out
            dp0 = max(dp0, dp1 + prices[i])
            # holding currently: holding last time / non_holding and buy in this time
            dp1 = max(dp1, dp0 - prices[i])

        return dp0

        ans = 0
        for i in range(1, len(prices)):
            ans += (max(prices[i]-prices[i-1], 0))

        return ans

## test
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    #Output: 7
    print(Solution().maxProfit(prices))