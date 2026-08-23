class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(len(nums)):
            el=abs(nums[i])
            nums[el-1]=-abs(nums[el-1])
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res

