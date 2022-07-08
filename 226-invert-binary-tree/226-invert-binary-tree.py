# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive_traversal(root):
            if root is None:
                return None
            else:
                root.left,root.right = root.right,root.left
                recursive_traversal(root.left)
                recursive_traversal(root.right)
            return root
        return recursive_traversal(root)