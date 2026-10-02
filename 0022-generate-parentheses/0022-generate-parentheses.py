class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def solve(s,open,close):
            if open==0 and close==0:
                res.append(s)
                return 
            if open>0:
                solve(s+'(',open-1,close)
            if close>open:
                solve(s+')',open,close-1)
                
        solve("",n,n)
        return res
            




            