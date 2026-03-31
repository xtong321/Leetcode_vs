"""
Linear Regression (Forward)
https://neetcode.io/problems/linear-regression-forward

https://blog.csdn.net/weixin_44142858/article/details/121468047

Your task is to implement linear regression, a statistical model that ends up 
being the foundation of neural networks. You can learn more from the 
Complete Explanation of Linear Regression or by reading the description below.
Your must implement get_model_prediction() which returns a prediction value for each dataset value, 
and get_error() which calculates the error for given prediction data.

Inputs - get_model_prediction:
- X - the dataset to be used by the model to predict the output. 
      len(X) = n, and len(X[i]) = 3 for 0 <= i < n.
- weights - the current w1, w2, and w3 weights for the model. len(weights) = 3.

Inputs - get_error:
- model_prediction - the model's prediction for each training example. len(model_prediction) = n.
- ground_truth - the correct answer for each example. len(ground_truth) = n.
"""

from functools import singledispatchmethod
#from itertools import Predicate
import numpy as np
from numpy.typing import NDArray
from sklearn import model_selection

from sklearn import datasets
from sklearn.model_selection import train_test_split

# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:    
    def get_LR_coef(self, X: NDArray[np.float64], labels: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # labels is a Nx1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        # Y = WX   ## (1xN) = (1x4) * (4xN), it is homogeneous matrix
        # W = Y * X_(-1)
        # transpose: arr.transpose()
        # inverse: np.linalg.pinv(a)
        #X = X.transpose()
        N, d = X.shape()
        X2 = np.ones((N, d+1))
        # copy X to X2
        for i in range(N):
            for j in range(d):
                X2[i,j] = X[i, j]
        
        Y = labels.T
        W = Y * np.linalg.pinv(X2.T)
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        #raise NotImplementedError
        prediction = np.matmul(X, weights)   # (Nx3)*(3x1) = (Nx1)
        return np.round(prediction, 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        #raise NotImplementedError
        error = np.mean(np.square(model_prediction - ground_truth))  # (Nx1)
        return round(error, 5)


###########################################################
# 本文介绍了线性回归模型的原理和代价函数，阐述了梯度下降法和正规方程法
# 求解参数的公式推导，并通过python 代码实现了两种方法，对比两者在处理
# 大规模特征时的优劣
# ref：https://blog.csdn.net/weixin_44142858/article/details/121468047
#
# 梯度下降法求解
#

def load_data():
    boston = datasets.load_boston()
    dataX = boston.data
    dataY = boston.target
    print("shape of X: ". dataX.shape)
    return dataX, dataY

def normalization(dataX):
    '''
    z-score normalization
    Parameters:
        dataX: input feature vectors
    Returns:
        dataX1: normalized dataX
        mu: mean
        signa: standard derviation vector
    '''
    mu = dataX.mean(0)
    sigma = dataX.std(0)
    dataX1 = (dataX - mu) / sigma
    return dataX1, mu, sigma

class linear_regression():
    def __init__(self, dataX, dataY, alpha=0.1):
        ones = np.ones((dataX.shape[0], 1))
        self.dataX = np.c_[ones, dataX]
        self.dataY = dataY
        self.datasize = self.dataX.shape[0]
        self.alpha = alpha  # learning rate
        self.theta = np.zeros(self.dataX.shape[1]) # init para

    def fit(self):
        iterations = 100 # iteration times
        for i in range(iterations):
            y = np.dot(self.dataX, self.theta).reshape(self.datasize,)
            loss = 1 / self.datasize * sum((y-self.dataY)**2)
            print(f"iter {i}, loss {loss}")

            # update theta
            updated_theta = []
            for j, theta_j in enumerate(self.theta):
                x_j = self.dataX[:, j]
                updated_theta_j = theta_j - self.alpha * (1/self.datasize) * np.sum((y-self.dataY)*x_j)
                updated_theta.append(updated_theta_j)
            self.theta = np.array(updated_theta)
        print(f"training finished")

    def predict(self, textX):
        ones = np.ones((testX.shape[0], 1))
        textX = np.c_[ones, textX]
        y_hat = np.dot(testX, self.theta)
        return y_hat


if __name__ == "__main2__":
    # 1 get dataset
    dataX, dataY = load_data()

    # 2. split dataset
    trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size=0.3, random_state=0)
    # 3. normalization
    newTrainX, mu, sigma = normalization(trainX)
    print(f'mu = {mu}, sigma = {sigma}')
    newTestX = (testX - mu) / sigma
    # 4. build a linear regression model
    model = linear_regression(newTrainX, trainY)
    # 5. train the model
    model.fit()
    # 6. test model
    y_hat = model.predict(newTestX)
    # 7. output error between predict and GT
    print(f"predict: {y_hat}")
    print(f"ground-truth: {testY}")
    print(f"diff: {1/testX.shape[0]*np.sum((y_hat-testY)**2)}")


###########################################################
# solve with formulate
# y = Xt * W
# W = inv(XtX) * Xt * y
#
import pandas as pd
import numpy as np

def load_data():
    #boston = datasets.load_boston()
    #dataX = boston.data
    #dataY = boston.target
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    dataX = data
    dataY = target    
    print(f"=> shape of X: {dataX.shape}")
    return dataX, dataY

def get_theta(dataX, dataY):
    '''
    parameters:
        dataX: shape(m,n)
        dataY: shape(m,)
    returns:
        parameters
    notes:
        np.dot(A,B): matrix multiply
        np.linalg.inv(A): return inverse of A
        A.T(): return transpose of A
    '''
    XtX = np.dot(dataX.T, dataX)
    inv_XtX = np.linalg.inv(XtX)
    return np.dot(np.dot(inv_XtX, dataX.T), dataY)


if __name__ == "__main__":
    # 1. add dataset
    print(f'1. load data ...')
    dataX, dataY = load_data()

    # 2. split dataset
    print(f'2. split data ...')
    trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size=0.3, random_state=0)

    # 3. add 1 to feature
    print(f'3. add one-col to data ...')
    ones = np.ones((trainX.shape[0], 1))
    trainX = np.c_[ones, trainX]

    # 3. solve para
    print(f'4. solve para ...')
    theta = get_theta(trainX, trainY)

    #4. predict
    print(f'5. predict and eval ...')
    ones1 = np.ones((testX.shape[0], 1))
    testX = np.c_[ones1, testX]
    n = testX.shape[0]
    y_hat = np.dot(testX, theta)
    loss = 1/n * np.sum((y_hat - testY)**2)

    print(f"predict: {y_hat}")
    print(f"ground-truth: {testY}")
    print(f"diff: {loss}")

    print(f"== predict   ground-truth ==")
    #result = [y_hat[:], testY[:]]
    result = np.column_stack((y_hat, testY))
    print(result)


## ==================================================================
# gradient descent method from neetcode
# https://neetcode.io/problems/linear-regression-training

import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        for _ in range(num_iterations):
            model_prediction = self.get_model_prediction(X, initial_weights)

            d1 = self.get_derivative(model_prediction, Y, len(X), X, 0)
            d2 = self.get_derivative(model_prediction, Y, len(X), X, 1)
            d3 = self.get_derivative(model_prediction, Y, len(X), X, 2)

            initial_weights[0] = initial_weights[0] - d1 * self.learning_rate
            initial_weights[1] = initial_weights[1] - d2 * self.learning_rate
            initial_weights[2] = initial_weights[2] - d3 * self.learning_rate

        return np.round(initial_weights, 5)

