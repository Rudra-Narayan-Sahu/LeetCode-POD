class Solution(object):
    def gcdOfOddEvenSums(self, n):
        so=n*n
        se=n*(n+1)
        res=min(so,se)
        if so==0 or se==0:
            return max(so,se)
        b=min(so,se)
        a=so+se-b
        while b!=0:
            a,b=b,a%b
        return a



        