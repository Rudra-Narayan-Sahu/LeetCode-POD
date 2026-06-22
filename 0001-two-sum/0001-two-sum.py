nums = [2, 7, 11, 15]
target = 9
class Solution:
    def twoSum(self,nums,target):
        seen={}#create a empty dictinary to store the vale and index 
        for i,num in enumerate(nums):
            comp=target-num
            if comp in seen:
                return(seen[comp],i)
            seen[num]=i
s1=Solution()
print(s1.twoSum(nums, target))  # Output: [0, 1]