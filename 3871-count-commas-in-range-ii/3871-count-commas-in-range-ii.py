class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        countComma=0
        start=1000
        while start<=n:
            countComma+=n-start+1
            start*=1000
        return countComma