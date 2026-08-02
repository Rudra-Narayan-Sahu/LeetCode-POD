class Solution(object):
    def stoneGame(self, piles):
        n=len(piles)
        total=sum(piles)
        memo={}
        player_1=self.game(piles,0,n-1,memo)
        player_2=total-player_1
        return player_1>=player_2
    def game(self,nums,i,j,memo):
        if i>j:
            return 0
        if i==j:
            return nums[i]
        if (i,j) in memo:
            return memo[(i,j)]
        c1=nums[i]+min(self.game(nums,i+2,j,memo),self.game(nums,i+1,j-1,memo))
        c2=nums[j]+min(self.game(nums,i,j-2,memo),self.game(nums,i+1,j-1,memo))
        memo[(i,j)]=max(c1,c2)
        return memo[(i,j)]
