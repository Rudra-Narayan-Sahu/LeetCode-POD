class Solution(object):
    def countCommas(self, n):
        if len(str(n))<4:
            return 0
        
        return n-999