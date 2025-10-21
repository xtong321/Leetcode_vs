"""
Given an array arr[] of size n-1 with integers in the range of [1, n], the task is to find
 the missing number from the first N integers.

Note: There are no duplicates in the list.

Examples: 

Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , n = 8
Output: 5
Explanation: Here the size of the array is 8, so the range will be [1, 8]. 
The missing number between 1 to 8 is 5


Input: arr[] = {1, 2, 3, 5}, n = 5
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. 
The missing number between 1 to 5 is 4
"""

class Solution(object):
    def missing_number(self, n, arr):
        hash = [0]* (n+1)

        for num in arr:
            hash[num] += 1

        for idx in range(1, n+1):
            if hash[idx] == 0:
                return idx


    def missing_number2(n, arr):
        sum_arr = sum(arr)
        
        # Calculate the expected sum
        expected_sum = (n * (n + 1)) // 2
        
        # Return the missing number
        return expected_sum - sum_arr


    def missing_number3(n, arr):
        xor1 = 0
        xor2 = 0

        # XOR all array elements
        for num in arr:
            xor2 ^= num

        # XOR all numbers from 1 to n
        for i in range(1, n + 1):
            xor1 ^= i

        # Missing number is the XOR of xor1 and xor2
        return xor1 ^ xor2
        
        
if __name__ == "__main__":
    print(Solution().missing_number(5, [1,2,3,5]))
    print(Solution().missing_number(3, [3,0,1]))

        
