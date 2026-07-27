class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        lp=(nums[0]-1)*(nums[1]-1)
        rp=(nums[-1]-1)*(nums[-2]-1)
        return max(lp,rp)
        