class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mn=float('inf')
        mn_arr=[None]*(len(nums))
        mn_arr[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            mn_arr[i]=min(mn_arr[i+1],nums[i])
        mx=float('-inf')
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
            score=mx-mn_arr[i]
            if score<=k:
                return i
        return -1
