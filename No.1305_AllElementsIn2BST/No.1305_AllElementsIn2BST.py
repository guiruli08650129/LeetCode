# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def trace(root, prt):
            if root == None:
                return []
            if root.left == None and root.right == None:
                prt.append(root.val)
                return prt
            else:
                if root.left:
                    prt = trace(root.left, prt)
                prt.append(root.val)
                if root.right:
                    prt = trace(root.right, prt)
                return prt

        list1 = trace(root1, [])
        list2 = trace(root2, [])
        ans = list1 + list2
        ans.sort()

        return ans
