class Solution(object):
    def longestSubsequence(self, nums):
        n=len(nums)
        m=float('-inf')
        is_zero=all(num==0 for num in nums)
        if is_zero:
            return 0
        xor=nums[0]
        for i in range(1,n):
            xor^=nums[i]
        if xor!=0:
            return n
        else:
            return n-1
        
        # left=0
        # for right in range(1,n):
        #     xor^=nums[right]
        #     while xor==0:
        #         xor^=nums[left]
        #         left+=1
        #     m=max(m,right-left+1)
        # return m
        