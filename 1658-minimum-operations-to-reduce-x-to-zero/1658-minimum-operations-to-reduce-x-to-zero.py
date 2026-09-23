class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        k=sum(nums)-x
        s=i=0
        idx=-1
        for j,el in enumerate(nums):
            s+=nums[j]
            while s>k and i<len(nums):
                s-=nums[i]
                i+=1
            if s==k:
                idx=max(idx,j-i+1)
        if idx<0:
            return -1
        else:
            return len(nums)-idx