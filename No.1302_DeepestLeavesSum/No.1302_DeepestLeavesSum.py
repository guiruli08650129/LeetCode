# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def recursive(root, deep, max_deep, leaf):
            if root.left == None and root.right == None:
                if max_deep < deep:
                    max_deep = deep
                    leaf.append((root.val, deep))
            if root.left != None:
                recursive(root.left, deep + 1, max_deep, leaf)
            if root.right != None:
                recursive(root.right, deep + 1, max_deep, leaf)

        deep = 0
        max_deep = 0
        leaf = []
        ans = 0
        recursive(root, deep, max_deep, leaf)
        leaf.sort(reverse=True)
        max_deep = max([x for (_, x) in leaf])
        for i, j in leaf:
            if j == max_deep:
                ans += i
        return ans
