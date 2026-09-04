class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
            res=float('inf')
            n=len(nums)
            max_res=[None]*n
            min_res=[None]*n
            max_res[0]=nums[0]
            min_res[-1]=nums[-1]
            for i in range(1,n):
                max_res[i]=max(max_res[i-1],nums[i])
            for j in range(n-2,-1,-1):
                min_res[j]=min(min_res[j+1],nums[j])
            for i in range(len(nums)):
                score=max_res[i]-min_res[i]
                if score<=k and score<res:
                    return i
            return -1