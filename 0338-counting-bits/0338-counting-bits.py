class Solution(object):
    def countBits(self, n):
        dp=[0]*(n+1)
        power=1
        for i in range(1,n+1):
            if i==2*power:
                power*=2
            dp[i]=dp[i-power]+1
        return dp
            



        