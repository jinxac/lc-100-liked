# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root, k):
        res = []
        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        traverse(root)
        
        return res[k - 1]
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.recursive(root, k)
