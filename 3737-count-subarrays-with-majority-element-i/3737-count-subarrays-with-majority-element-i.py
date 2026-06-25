class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        count=0
        for i in range(len(nums)):
            frq=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    frq+=1
                l=j-i+1
                if frq*2>l:
                    count+=1
        return count
    # def isSub(self,nums,target):
    #     co=0
    #     for el in nums:
    #         if el==target:
    #             co+=1
    #     if co > len(nums) // 2:
    #         return True
    #     return False


        