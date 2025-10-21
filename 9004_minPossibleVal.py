"""
given an integer array data[], and maxOperations
select two elements, i and j, meet 0 <= i < j <= N-1, compute abs(data[i]-data[j]), append it to the array
find the possible minimum value from the data array
"""

class Solution(object):
    def findMinVal(self, data, maxOp):
        if not data or maxOp < 0:
            return None
        
        N = len(data)
        cur_min = min(data)
        if cur_min <= 0:
            return cur_min

        for k in range(maxOp):
            data.sort()
            data_dif = []
            for i in range(1, len(data)):
                dif = abs(data[i] - data[i-1])
                data_dif.append(dif)
            data_dif.sort()
            data.append(data_dif[0])
            cur_min = min(cur_min, data_dif[0])

        return cur_min

if __name__ == "__main__":
    data = [10, 6]
    oper = 4
    print(Solution().findMinVal(data, oper))

