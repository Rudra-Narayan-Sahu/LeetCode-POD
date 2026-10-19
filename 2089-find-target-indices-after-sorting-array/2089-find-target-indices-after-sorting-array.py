class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums.sort()
        # res=[]
        # for i,el in enumerate(nums):
        #     if el==target:
        #         res.append(i)
        #     elif el>target:
        #         break
        # return res

        #without sort
        lc,tc=0,0
        for el in nums:
            if el<target:
                lc+=1
            elif el==target:
                tc+=1
        res=list(range(lc,lc+tc))
        return res
        