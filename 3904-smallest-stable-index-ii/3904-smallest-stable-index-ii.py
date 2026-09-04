class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        mini=[None]*n
        mn=float('inf')
        for i in range(n-1,-1,-1):
            if nums[i]<mn:
                mn=nums[i]
            mini[i]=mn
        mx=float('-inf')
        for i in range(n):
            if nums[i]>mx:
                mx=nums[i]
            if mx-mini[i]<=k:
                return i
        return -1