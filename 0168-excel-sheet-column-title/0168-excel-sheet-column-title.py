class Solution(object):
    def convertToTitle(self,n):
        ans=''
        while n>0:
            n-=1
            res=n%26
            ans+=string.ascii_uppercase[res]
            n//=26
        return ans[::-1]
