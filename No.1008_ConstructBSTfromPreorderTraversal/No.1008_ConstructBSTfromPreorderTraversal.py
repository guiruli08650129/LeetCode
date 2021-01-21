# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(preorder):
            if len(preorder) == 0:
                return None
            elif len(preorder) == 1:
                root_val = preorder[0]
                root = TreeNode(root_val)
                return root
            else:
                root_val = preorder[0]
                root = TreeNode(root_val)
                left = [(i) for i in preorder if i < root_val]
                right = [(i) for i in preorder if i > root_val]
                root.left = build(left)
                root.right = build(right)
                return root

        return build(preorder)
