import numpy as np

cost = np.array([[0,1,2],[2,0,1]], dtype=np.float)
row_weight = np.array([2,1])
col_weight = np.array([1,1,1])

for _ in range(100):
    cost = cost / np.sum(cost, axis=1).reshape(2,-1) * row_weight.reshape(2,-1)
    print(cost)
    cost = cost / np.sum(cost, axis=0).reshape(-1,3) * col_weight.reshape(-1, 3)
    print(cost)

print('=====')
print(cost)