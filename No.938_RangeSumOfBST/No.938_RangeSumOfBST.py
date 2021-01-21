class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sumNode = 0
        def check(val, s):
            if val > low-1 and val < high+1:
                s+=val
            return s
        
        def trace(node, sumNode):
            if node.left == None and node.right == None:
                sumNode = check(node.val,sumNode)
                return sumNode
            else:
                sumNode = check(node.val,sumNode)
                if node.left:
                    sumNode = trace(node.left, sumNode)
                if node.right:
                    sumNode = trace(node.right, sumNode)
            return sumNode
        ans = trace(root, sumNode)
        return ans
    