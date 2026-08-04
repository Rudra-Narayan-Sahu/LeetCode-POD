class Solution(object):
    def findMissingElements(self, nums):
        res=[]
        small=min(nums)
        big=max(nums)
        nums.sort()
        for i in range(small,big+1):
            if i not in nums:
                res.append(i)
        return res

        