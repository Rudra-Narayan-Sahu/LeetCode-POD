class Solution(object):
    def stoneGameIII(self, stoneValue):
        n=len(stoneValue)
        dp=[-1]*n
        res=self.game(stoneValue,0,dp)
        if res<0:
            return "Bob"
        elif res>0:
            return "Alice"
        else:
            return "Tie"

    def game(self,nums,i,dp):
        n=len(nums)
        if i>=n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        res=nums[i]-self.game(nums,i+1,dp)
        #  Correct: compare existing 'res' with the new choice
        if i + 1 < n:
            res = max(res, nums[i] + nums[i+1] - self.game(nums, i+2, dp))
        if i + 2 < n:
            res = max(res, nums[i] + nums[i+1] + nums[i+2] - self.game(nums, i+3, dp))
        
        dp[i]=res
        return dp[i]
        
