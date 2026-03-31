"""
1161. 最大层内元素和

给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
返回总和 最大 的那一层的层号 x。如果有多层的总和一样大，返回其中 最小 的层号 x。

输入：root = [1,7,0,7,-8,null,null]
       1
    7      0
 7    -8

输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
"""

from typing import Optional, List
from collections import deque
from collections import defaultdict

# ====== 二叉树节点定义 ======
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum1(self, root: Optional[TreeNode]) -> int:
        """
        Idea: 
          1) traverse the tree and add the level info for each node
          2) sum the nodes in each level, and get the min_sum
        """
        max_sum = root.val
        max_level = 0
        sum = defaultdict(int) # dict[level] = x, means the sum at level is x
        def dfs(node: TreeNode, level: int):
            if not node:
                return
            if node:
                sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # find the max-val item in dict
        return max(sum, key=sum.get)+1

    def maxLevelSum2(self, root: TreeNode) -> int:
        q, maxSum, res, level = [root], 0, 0, 0
        while any(q):
            curSum = 0
            for _ in range(len(q)):
                node = q.pop(0)
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
            if curSum > maxSum:
                maxSum, res = curSum, level
        return res


    # ====== 你在 LeetCode 上的解法，直接贴到这里 ======
    def maxLevelSum3(self, root):
        if not root:
            return 0
        q = deque([root])
        level = 0
        best_sum = float('-inf')
        best_level = 0

        while q:
            level += 1
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > best_sum:
                best_sum = s
                best_level = level

        return best_level
# ============================================


# ====== 从层序数组构建二叉树（None 表示空） ======
def build_tree(level_list):
    if not level_list or level_list[0] is None:
        return None

    root = TreeNode(level_list[0])
    q = deque([root])
    i = 1

    while q and i < len(level_list):
        node = q.popleft()

        # 左子节点
        if i < len(level_list) and level_list[i] is not None:
            node.left = TreeNode(level_list[i])
            q.append(node.left)
        i += 1

        # 右子节点
        if i < len(level_list) and level_list[i] is not None:
            node.right = TreeNode(level_list[i])
            q.append(node.right)
        i += 1

    return root


# ====== main 测试程序 ======
if __name__ == "__main__":
    # 示例：对应 LeetCode 示例 [1,7,0,7,-8,null,null]
    level_order = [1, 7, 0, 7, -8, None, None]

    root = build_tree(level_order)

    sol = Solution()
    ans1 = sol.maxLevelSum1(root)
    ans2 = sol.maxLevelSum2(root)
    ans3 = sol.maxLevelSum3(root)
    print("最大层内元素和所在层：", ans1, ans2, ans3)

