class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans,n=0,len(nums)
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                count=len(seen)
                ans+=count**2
        return ans