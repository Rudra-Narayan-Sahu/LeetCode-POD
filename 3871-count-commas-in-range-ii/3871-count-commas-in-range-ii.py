class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=999:
            return 0
        start=1000
        count=0
        while start<=n:
            count+=n-start+1
            start*=1000
        return count