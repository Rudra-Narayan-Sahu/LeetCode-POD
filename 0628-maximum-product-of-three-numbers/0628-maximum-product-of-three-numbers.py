class Solution(object):
    def maximumProduct(self, nums):
        n=len(nums)
        nums.sort()
        lp=nums[0]*nums[1]*nums[-1]
        rp=nums[-1]*nums[-2]*nums[-3]
        return max(lp,rp)
        
        