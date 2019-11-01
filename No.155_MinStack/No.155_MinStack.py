class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.list = self.list[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)