"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, 
return the number of pairs (ri, cj) such that 
row ri and column cj are equal.
A row and column pair is considered equal if they 
contain the same elements in the same order 
(i.e., an equal array).

"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return False

        R = len(grid)
        C = len(grid[0])
        if R!=C:
            return False
        ans = []
        flag = True
        for i in range(0, R):
            row = grid[i]
            for j in range(0, C):
                col = [ri[j] for ri in grid]
                  
                flag = True
                for k in range(0, C):
                    if row[k] - col[k]!=0:
                        flag = False
                        break

                if flag:
                    ans.append([i, j])

        return ans
    
if __name__ == "__main__":
    grid = [[3,2,1],[1,7,6],[2,7,7]] # Output: 1
    print(Solution().equalPairs(grid))

    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] # Output: 3
    print(Solution().equalPairs(grid))