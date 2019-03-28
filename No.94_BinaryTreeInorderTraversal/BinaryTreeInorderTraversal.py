# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        output = []
        stack = []
        current = root
        done = False

        while (not done):
            if (current != None):
                stack.append(current)
                current = current.left
            else:
                if (len(stack) > 0):
                    current = stack.pop()
                    output.append(current.val)
                    current = current.right
                else:
                    done = True

        return output
