class Solution(object):
    def predictTheWinner(self, nums):
        n=len(nums)
        total_score=sum(nums)
        player_1_score=self.helper(nums,0,n-1)
        player_2_score=total_score-player_1_score
        return player_1_score>=player_2_score
    def helper(self,nums,i,j):
        if i>j:
            return 0
        if i==j:
            return nums[i]
        choce_1=nums[i]+min(self.helper(nums,i+2,j),self.helper(nums,i+1,j-1))
        choce_2=nums[j]+min(self.helper(nums,i,j-2),self.helper(nums,i+1,j-1))
        return max(choce_1,choce_2)

        