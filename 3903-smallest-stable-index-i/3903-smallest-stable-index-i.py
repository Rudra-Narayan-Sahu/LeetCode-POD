class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=float('inf')
        idx=-1
        for i in range(len(nums)):
            score=max(nums[:i+1])-min(nums[i:])
            #print(score)
            if k>=score and score<res:
                return i
        return idx