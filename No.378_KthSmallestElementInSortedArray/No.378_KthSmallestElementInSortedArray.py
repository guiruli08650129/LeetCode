class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        flatten = []
        for n in matrix:
            flatten += n

        flatten.sort()
        return flatten[k-1]