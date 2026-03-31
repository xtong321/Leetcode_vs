"""
https://neetcode.io/problems/gradient-descent

Your task is to minimize the function via Gradient Descent: 
f(x) = x**2

Gradient Descent is an optimization technique widely used in machine learning for training models. It is crucial for minimizing the cost or loss function and finding the optimal parameters of a model.
For the above function the minimizer is clearly x = 0, but you must implement an iterative approximation algorithm, through gradient descent.

Input:
- iterations - the number of iterations to perform gradient descent. iterations >= 0.
- learning_rate - the learning rate for gradient descent. 1 > learning_rate > 0.
- init - the initial guess for the minimizer. init != 0.

Given the number of iterations to perform gradient descent, the learning rate, and an initial guess, return the value of x that globally minimizes this function.
Round your final result to 5 decimal places using Python's round() function.

Example 1:
Input: iterations = 0, learning_rate = 0.01, init = 5
Output: 5

Example 2:
Input: iterations = 10, learning_rate = 0.01, init = 5
Output: 4.08536

Idea:
1) dL/dx = d(x**2)/dx = 2x
2) x_(j+1) = x_j - l * dL/dx
"""

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        lr = learning_rate

        for _ in range(iterations):
            dx = 2 * x          # derivative
            x = x - lr * dx     # x = x - eta*dL/dx

        return round(x, 5)

if __name__ == "__main__":
    #Input: iterations = 0, learning_rate = 0.01, init = 5; Output: 5
    print(Solution().get_minimizer(iterations = 0, learning_rate = 0.01, init = 5))

    #Input: iterations = 10, learning_rate = 0.01, init = 5; Output: 4.08536
    print(Solution().get_minimizer(iterations = 10, learning_rate = 0.01, init = 5))

    print(Solution().get_minimizer(iterations = 100, learning_rate = 0.01, init = 5))

    print(Solution().get_minimizer(iterations = 1000, learning_rate = 0.01, init = 5))
  