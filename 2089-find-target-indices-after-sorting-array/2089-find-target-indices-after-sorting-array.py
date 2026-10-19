class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        for i,el in enumerate(nums):
            if el==target:
                res.append(i)
            elif el>target:
                break
        return res
        