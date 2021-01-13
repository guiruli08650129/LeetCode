# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def recursive(o, c, target):
            if o.val == target.val:
                return c
            elif o.left == None and o.right == None:
                return None
            else:
                if o.left:
                    ans = recursive(o.left, c.left, target)
                    if ans:
                        return ans
                if o.right:
                    ans = recursive(o.right, c.right, target)
                    if ans:
                        return ans

        o = original
        c = cloned
        return recursive(o, c, target)
