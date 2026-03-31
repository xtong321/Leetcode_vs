"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path 
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, root.val)

"""
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }

    int dfs(TreeNode* node, int maxSoFar) {
        if (!node) return 0;

        int good = node->val >= maxSoFar ? 1 : 0;
        maxSoFar = max(maxSoFar, node->val);

        return good + dfs(node->left, maxSoFar) + dfs(node->right, maxSoFar);
    }
};
"""