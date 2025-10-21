"""
描述：给定一个严格递增的正整数数组 arr。
要求：从数组 arr 中找出最长的斐波那契式的子序列的长度。如果不存斐波那契式的子序列，则返回 0。

说明：
斐波那契式序列：如果序列 X1, X2, ..., Xn, 满足：n≥3；
对于所有 i+2≤n，都有 X(i) + X(i+1)=X(i+2),则称该序列为斐波那契式序列。

斐波那契式子序列：从序列 A 中挑选若干元素组成子序列，并且子序列满足斐波那契式序列，则称该序列为斐波那契式子序列。
例如：
A=[3,4,5,6,7,8]。则 [3,5,8] 是 A 的一个斐波那契式子序列。
3≤arr.length≤1000。

示例：
示例 1：
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8]。

示例 2：
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18]。
"""

class solution():
    def longestFibSubseq_1(self, nums):
        size = len(nums)
        if size < 3:
            return 0
        ans = 0

        for i in range(size):
            for j in range(i+1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                temp_k = j+1
                while temp_k < size:
                    if nums[temp_i] + nums[temp_i] == nums[temp_k]:
                        temp_ans += 1
                        temp_i = temp_j
                        temp_j = temp_k
                    temp_k +=1
                
                if ans < temp_ans:
                    ans = temp_ans
        
        return ans+2 if ans > 0 else ans
        """if ans > 0:
            return ans + 2
        else:
            return ans
        """
    
    def longestFibSubseq_2(self, nums):
        size = len(nums)
        if size < 3:
            return 0
        ans = 0

        idx_map = dict()
        for idx, num in enumerate(nums):
            idx_map[num] = idx

        for i in range(size):
            for j in range(i+1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                while nums[temp_i] + nums[temp_j] in idx_map:
                    temp_ans += 1
                    temp_k = idx_map[nums[temp_i] + nums[temp_j]]
                    temp_i = temp_j
                    temp_j = temp_k        
                
                if ans < temp_ans:
                    ans = temp_ans
        
        return ans+2 if ans > 0 else ans
        

    def longestFibSubseq_3(self, nums):
        size = len(nums)
        if size < 3:
            return 0

        sub = [] # to store the Fib subseq
        dp = [0 for _ in range(size+1)]
        for i in range(0, size+1):
            if nums[i] == sub[len(sub)-2] + sub[len(sub)-1]:
                dp[i] = dp[i-1] + 1
                sub.append(nums[i])

        return dp[size]


if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8]   # return 5
    arr2 = [1,3,7,11,12,14,18] # return 3
    print(solution().longestFibSubseq_2(arr1))
    print(solution().longestFibSubseq_2(arr2))