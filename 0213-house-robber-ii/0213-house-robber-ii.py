class Solution(object):
    def helper(self,nums,st,end):
        n=end-st+1
        
        if n==1:
            return nums[st]
        dp=[0]*n
        dp[0]=nums[st]
        dp[1]=max(nums[st],nums[st+1])
        for j in range(2,n):
            dp[j]=max(dp[j-1],dp[j-2]+nums[st+j])
            
        return dp[n-1]
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        return max(self.helper(nums,0,n-2),self.helper(nums,1,n-1))
        