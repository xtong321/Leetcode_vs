"""
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""

class Solution:
    def tribonacci1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        Tn = self.tribonacci(n-3) + self.tribonacci(n-2)+ self.tribonacci(n-1)
        return Tn
    
    def tribonacci2(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn

        return tn
    
    # memorize the procedure
    def tribonacci3(self, n):
        memo = [0 for _ in range(n + 1)]
        return self.my_tribonacci(n, memo)
    
    def my_tribonacci(self, n, memo):
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        if n<=2:
            return memo[n]

        if memo[n] != 0:
            return memo[n]
        
        memo[n] = self.my_tribonacci(n-1, memo) + self.my_tribonacci(n-2, memo) + self.my_tribonacci(n-3, memo)

        return memo[n]
    
    # DP, dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    def tribonacci4(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]
            


if __name__ == "__main__":
    n = 4; Output = 4
    print(f"n = {n}, GT = {Output}, pred =", Solution().tribonacci(n))

    n = 25; Output = 1389537
    print(f"n = {n}, GT = {Output}, pred =", Solution().tribonacci(n))