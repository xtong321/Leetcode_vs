"""
https://leetcode.com/problems/leaf-similar-trees
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def get_leaf(self, node):
        # get leaf seq of a tree
        if not node:
            return []
        if not node.left and not node.right:            
            return [node.val]

        return self.get_leaf(node.left) + self.get_leaf(node.right)
        #return leaf #max(self.maxDepth(root.left), self.maxDepth(root.right))+1


    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """        
        leaf1 = self.get_leaf(root1)      
        leaf2 = self.get_leaf(root2)
        return leaf1 == leaf2


    def leafSimilar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return getLeaves(node.left) + getLeaves(node.right)

        return getLeaves(root1) == getLeaves(root2)

    
    
