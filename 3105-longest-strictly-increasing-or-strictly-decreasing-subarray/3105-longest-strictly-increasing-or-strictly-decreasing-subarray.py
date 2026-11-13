class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        si,sd=1,1
        mx=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                si+=1
                sd=1
            elif nums[i]<nums[i-1]:
                sd+=1
                si=1
            else:
                si=1
                sd=1
            mx=max(mx,si,sd)
        return mx