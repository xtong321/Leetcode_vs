"""
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。


示例 1：

输入：root = [1,null,2,3]

输出：[3,2,1]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [(root, 'visit')]
        while stack:
            node, label = stack.pop()
            if label == 'visit':
                stack.append((node, 'get'))
                if node.right:
                    stack.append((node.right, 'visit'))
                if node.left:
                    stack.append((node.left, 'visit'))
            else:
                result.append(node.val)
        return result

if __name__ == "__main__":
    None