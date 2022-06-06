# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 0
            else:
                l_depth = dfs(node.left)
                r_depth = dfs(node.right)

                if l_depth > r_depth:
                    return l_depth+1
                else:
                    return r_depth+1

        a = dfs(root)
        return a