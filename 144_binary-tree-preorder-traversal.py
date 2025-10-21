"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：

输入：root = [1,null,2,3]

输出：[1,2,3]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while root or stack:
            if not root:
                root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left

        return result

if __name__ == "__main__":
    None