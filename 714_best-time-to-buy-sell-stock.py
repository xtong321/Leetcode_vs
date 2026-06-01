"""
714. Best Time to Buy and Sell Stock with Transaction Fee
You are given an array prices where prices[i] is the price of a 
given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many 
transactions as you like, but you need to pay the transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
"""

from typing import List 
from functools import cache    

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        greddy algo
        3 cases:
        1) profilt day, not sell day, can compute the profile
        2) sell in previous day, and start to search a min-price
        3) no operation, keep previous state (no buyin and sellout operation)
        """
        ans = 0
        min_price = prices[0]
        for k in range(1, len(prices)):
            # case-2: buy in
            if prices[k] < min_price:
                min_price = prices[k]
            
            # case-3: keep previous state, no operation
            if prices[k]>=min_price and prices[k]<=min_price+fee:
                continue

            # case-1: compute profile
            if prices[k] > min_price + fee:
                ans += (prices[k]-min_price - fee)
                min_price = prices[k] - fee

        return ans

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        """
        memorized search
        dfs(i, j): starting from day-i, state = j, the max-profile
        j = 0: not hold stock
        j = 1: hold stock
        the ans is dfs(0, 0)

        state transform function:
        1) no operation: dfs(i, j) = dfs(i+1, j)
        2) j>0, sell out: dfs(i, j) = prices[i] + dfs(i+1, 0) - fee
        3) j=0, buy in: dfs(i, j) = -prices[i] + dfs(i+1, 1)
        """
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= len(prices):
                return 0
            ans = dfs(i+1, j)
            if j:
                ans = max(ans, prices[i]+dfs(i+1, 0) - fee)
            else:
                ans = max(ans, -prices[i]+dfs(i+1, 1))
            return ans

        return dfs(0, 0)

    def maxProfit3(self, prices: List[int], fee: int) -> int:
        """
        define f[i][j] as the max_profile at day-i, state = j
        j = 0: means not hold stock
        j = 1: hold stock
        initial value: f[0][0]=0, f[0][1] = -prices[0]

        when i>=1, if j=0 (no stock), 
            then f[i][0] <= f[i-1][0] and f[i-1][1]+prices[i]-fee
        if j=1 (hold stack)
            f[i][1] <= f[i-1][1] and f[i-1][0]-prices[i]
        """        
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][1] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i] - fee)
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - prices[i])
        return f[n - 1][0]


    def maxProfit4(self, prices: List[int], fee: int) -> int:
        """
        DP: compute profit according to non_hoilding or holding stock at last time
        """
        # 初始化没有股票和持有股票的情况
        dp0 = 0; dp1 = -prices[0]
        N = len(prices)
        for i in range(1, N):
            # 当前没有股票：上一次就没有 / 上一次持有本次卖掉并扣除手续费
            dp0 = max(dp0, dp1+prices[i]-fee)
            # 当前持有股票：上一次就持有 / 上一次没有股票本次买入
            dp1 = max(dp1, dp0 - prices[i])

        return dp0

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]; fee = 2; Output = 8
    print(f"test-1: GT = {Output}, pred = ", Solution().maxProfit3(prices, fee))

    prices = [1,3,7,5,10,3]; fee = 3; Output = 6
    print(f"test-2: GT = {Output}, pred = ", Solution().maxProfit3(prices, fee))