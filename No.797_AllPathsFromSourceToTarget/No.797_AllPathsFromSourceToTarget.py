class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        partial = []

        def findPath(node):
            if node == len(graph) - 1:
                ans.append(partial.copy())
                return
            for i in graph[node]:
                partial.append(i)
                findPath(i)
                partial.pop()

        partial.append(0)
        findPath(0)
        return ans
