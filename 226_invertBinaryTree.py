"""
描述：给定一个二叉树的根节点 root。
要求：将该二叉树进行左右翻转。
"""

class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree1(self, root):
        if not root:
            return None
        left = self.invertTree1(root.left)
        right = self.invertTree1(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree2(self, Node):
        if not Node:
            return None
        
        left = Node.left
        right = Node.right
        Node.left = right
        Node.right = left
        self.invertTree2(self, Node.left)
        self.invertTree2(self, Node.right)
        return Node

    # iteration algo
    def invertTree3(self, root) :
        if not root:
            return None

        stack = []
        stack.push(root)
        while not stack.empty():
            node = stack.top()          # 中
            stack.pop()
            #swap(node->left, node->right);
            left = node.left
            node.left = node.right
            node.right = left
            if not node.right:
                stack.push(node.right)  # 右
            if not node.left:
                stack.push(node.left)   # 左
        
        return root
    

