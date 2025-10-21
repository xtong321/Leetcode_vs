"""
原题
求一棵二叉树的最小高度，即从根节点到最近叶子节点的路径经过的节点数。
注意点：
无
例子:
输入:
3
/ \
9 20
/ \
15 7
/
14
输出: 2
解题思路
可以通过树的广度优先遍历 Binary Tree Level Order Traversal 来实现，在广度优
先遍历的过程中，每遍历一层就高度加一，如果某一个节点是叶子节点，那么当前
的高度就是最小高度。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth, curr_level = 0, [root]
        while curr_level:
            depth += 1
            next_level = []
            for n in curr_level:
                left, right = n.left, n.right
                if left is None and right is None:
                    return depth
                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)
            curr_level = next_level
        return depth


if __name__ == "__main__":
    None