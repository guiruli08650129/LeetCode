# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if root == None:
            return []

        ans = []

        def trace(node, path):
            path.append(node.val)
            if node.left == None and node.right == None:
                ans.append(path.copy())
            if node.left:
                trace(node.left, path)
            if node.right:
                trace(node.right, path)
            path.pop()

        path = []
        trace(root, path)
        return ["->".join([str(x) for x in b]) for b in ans]
