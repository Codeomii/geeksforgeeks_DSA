'''Size of Binary Tree:--

Given the root of a binary tree, return the size of the tree. The size of a binary tree is the total number of nodes in the tree.

Examples:

Input:   1
       /   \
      2     3
      
Output:  3
Explanation: There are 3 nodes in the given binary tree, so its size is 3.
Input:   1
       /   \
      2     3
     / \   / \
    4   5 6   7
Output: 7
Explanation: There are 7 nodes in the given binary tree, so its size is 7.

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105'''

# Solution:--

class Solution:
    def getSize(self, root):
        if root is None:
            return 0
        
        left_size = self.getSize(root.left)
        right_size = self.getSize(root.right)
        
        return 1 + left_size + right_size