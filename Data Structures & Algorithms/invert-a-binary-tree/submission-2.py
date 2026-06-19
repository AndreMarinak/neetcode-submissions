# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def reverse1(self, node):
        temp=node.right
        node.right=node.left
        node.left=temp
# Only recurse if the left child actually exists!
        if node.left != None:
            self.reverse1(node.left)
            
        # Only recurse if the right child actually exists!
        if node.right != None:
            self.reverse1(node.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None
        else:
            self.reverse1(root)
        
        return root