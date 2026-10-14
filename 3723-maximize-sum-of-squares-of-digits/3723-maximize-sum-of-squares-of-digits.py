class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum>9*num:
            return ""
        ans=[]
        for i in range(num):
            d=min(9,sum)
            ans.append(str(d))
            sum-=d
        return "".join(ans) if sum==0 else ""