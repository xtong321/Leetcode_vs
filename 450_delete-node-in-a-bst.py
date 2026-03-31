"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with 
the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

example:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
       5                            5
    3       6            =>      4      6
 2    4         7             2              7

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMin(self, node: TreeNode):
        # BST 最左边的是最小值
        while node.left != None:
            node = node.left
        return node
     
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: #        if key==root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left            
            #minNode = TreeNode(None)
            #minNode = self.getMin(root.right)
            #root.val = minNode.val
            #root.right = self.deleteNode(root.right, minNode.val)
            # find inorder successor
            successor = root.right
            while successor.left:
                successor = successor.left
            
            successor.left = root.left
            root = root.right
        
        return root

        