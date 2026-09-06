class Solution(object):
    def countGoodRotations(self, nums):
        n=len(nums)
        total=sum(nums)
        mid=len(nums)//2
        first=sum(nums[:mid])
        res = 1 if first > total - first else 0
        for i in range(1,len(nums)):
            first += nums[(i + mid - 1) % n] - nums[i - 1]
            if first>total-first:
                res+=1
        return res
