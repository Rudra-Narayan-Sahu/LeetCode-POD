class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i,ch in enumerate(s):
            prod=(i+1)*(26-(ord(ch)-ord('a')))
            res+=prod
        return res
            
        