class Solution(object):
    def numDistinct(self, s, t):
        m,n=len(s),len(t)
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.solve(s,t,0,0,dp)
    def solve(self,s,t,i,j,dp):
        if j==len(t):
            return 1
        if i==len(s):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            take=self.solve(s,t,i+1,j+1,dp)
            skip=self.solve(s,t,i+1,j,dp)
            dp[i][j]=take+skip
        else:
            dp[i][j]=self.solve(s,t,i+1,j,dp)
        return dp[i][j]
        