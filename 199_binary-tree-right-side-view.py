"""
199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]
解释：
       1
   2       3
     5        4

"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None: return
            if depth == len(ans):  # 这个深度首遇次到
                ans.append(node.val)
            dfs(node.right, depth + 1)  # 先递归右子树，保证首次遇到的一定是最右边的节点
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return ans


    def rightSideView2(self, root: TreeNode) -> List[int]:
        """
        return list of right view
        Args:
          1) root (tree node): 
        Return:
          1) list: the node list from top to bottom from right view
        """
        if not root:
            return None

        ans = []
        def dfs(node: TreeNode, depth: int) -> None:
            """
            dfs search to the next setp
            prev_dir: direction of previous step, 0-left, 1-right
            depth: current depth of visited node
            """
            if not node:
                return

            if depth == len(ans):
                ans.append(node.val)

            dfs(node.right, depth+1) # first scan right branch
            dfs(node.left, depth+1)  # then scan left search

        dfs(self, root, 0)

        return ans
            

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder_traversal_recursion(root):
    if root is None:
        return
    print(root.val)
    preorder_traversal_recursion(root.left)
    preorder_traversal_recursion(root.right)

def preorder_traversal(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data, index):
        if index >= len(data) or data[index] == "NaN":
            return None
        root = TreeNode(int(data[index]))
        root.left = self.build_tree(data, 2 * index + 1)
        root.right = self.build_tree(data, 2 * index + 2)
        return root

    def init_tree(self, data):
        if not data or data[0] == 'NaN':
            return None
        return self.build_tree(data, 0)

    def test():
        data = ["1", "2", "3", "NaN", "5", "6", "7"]
        tree = BinaryTree()
        root = tree.init_tree(data)
        print("1. 先序非递归")
        preorder_traversal(root)
        print("\n2. 先序递归")
        preorder_traversal_recursion(root)

if __name__ == '__main__':
test()