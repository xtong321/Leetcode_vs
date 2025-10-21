"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

示例 1：
     1
         2
     3

输入：root = [1,null,2,3]
输出：[1,3,2]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        while p or stack:
            # Save the nodes which have left child
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                # Visit the middle node
                result.append(p.val)
                # Visit the right subtree
                p = p.right

        return result

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2;   n1.right = n5
    n2.left = n3;   n2.right = n4    
    n5.left = n6
    n6.left = n7
    print(Solution().inorderTraversal(n1)) # [1, 3, 2]
 