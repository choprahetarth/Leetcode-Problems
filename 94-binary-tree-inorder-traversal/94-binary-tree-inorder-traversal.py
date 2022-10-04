# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        def recursive_inorder(root): #LNR
            if root is None:
                return
            else:
                recursive_inorder(root.left)    
                output.append(root.val)
                recursive_inorder(root.right)
        recursive_inorder(root)
        return output
            