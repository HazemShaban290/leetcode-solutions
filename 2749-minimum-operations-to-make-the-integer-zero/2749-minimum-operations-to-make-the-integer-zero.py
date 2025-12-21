class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 33):               # we try k operations
            rest = num1 - k * num2
            if rest < k:                     # must be >= k
                continue
            if bin(rest).count('1') <= k:    # must fit in k powers of 2
                return k
        return -1
        