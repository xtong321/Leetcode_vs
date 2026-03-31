"""
1372. 二叉树中的最长交错路径

给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。

输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0  # 记录最大 ZigZag 长度

        def dfs(node: Optional[TreeNode], direction: int, length: int):
            """
            direction: 0 表示上一步是向左走的，1 表示向右走的
            length: 当前 ZigZag 路径长度
            """
            if not node:
                return
            # 更新最大值
            self.max_len = max(self.max_len, length)

            if direction == 0:  # 上一步向左，这一步必须向右
                dfs(node.right, 1, length + 1)  # 继续 ZigZag
                dfs(node.left, 0, 1)  # 从左子节点重新开始
            else:  # 上一步向右，这一步必须向左
                dfs(node.left, 0, length + 1)
                dfs(node.right, 1, 1)

        # 从根节点开始，尝试两个方向
        dfs(root.left, 0, 1)   # 假设第一步向左
        dfs(root.right, 1, 1)  # 假设第一步向右

        return self.max_len

# ===== 测试用例 =====
if __name__ == "__main__":
    # 构造测试树
    #       1
    #      / \
    #     2   3
    #      \   \
    #       4   5
    #      /   /
    #     6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)

    sol = Solution()
    print(sol.longestZigZag(root))  # 输出示例：3
