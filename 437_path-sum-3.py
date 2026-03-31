"""
https://leetcode.com/problems/path-sum-iii

437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number 
of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must
 go downwards (i.e., traveling only from parent nodes to child nodes).

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Solution:
前缀和 + DFS（O(n)）
这是这题的最佳解法，也是面试官最喜欢的写法。

核心思想：
使用一个哈希表 prefix_sum_count 记录“前缀和出现次数”
当前路径和为 curr_sum
如果存在 curr_sum - targetSum，说明从某个前缀到当前节点的路径和为 targetSum
DFS 遍历树，同时更新前缀和计数
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix_sum_count = {0: 1}  # 前缀和为0出现1次（空路径）
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sum_count.get(curr_sum - targetSum, 0)
            
            prefix_sum_count[curr_sum] = prefix_sum_count.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix_sum_count[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

    def pathSum2(self, root, targetSum):
        if not root:
            return 0

        count = self.dfsPathSum(root, targetSum)

        count += self.pathSum2(root.left, targetSum)
        count += self.pathSum2(root.right, targetSum)

        return count

    def dfsPathSum(self, node, targetSum):
        if not node:
            return 0

        count = 0

        if node.val == targetSum:
            count += 1

        count += self.dfsPathSum(node.left, targetSum-node.val)
        count += self.dfsPathSum(node.right, targetSum-node.val)

        return count

