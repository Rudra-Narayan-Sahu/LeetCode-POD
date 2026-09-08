class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>0 and n<=999:
            return 0
        return n-999
        