class Solution(object):
    def isDivide(self,n,i):
        res=n/i
        if isinstance(res,int):
            return True
        else:
            return False
    def isThree(self, n):
        count=0
        for i in range(2,n):
            if n%i==0:
                count+=1
        if count==1:
                return True
        return False
        