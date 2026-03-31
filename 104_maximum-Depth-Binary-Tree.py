"""
求一颗二叉树的最大深度，最大深度指跟节点到最底层叶子节点的距离。
注意点：
无
例子:
输入:
  3
 / \
9  20
   / \
  15 7
 /
14
输出: 4
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:    # root is None
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


if __name__ == "__main__":
    print(Solution.maxDepth())
