class Solution(object):
    def uniqueXorTriplets(self, nums):
        n=len(nums)
        if n==1 or n==2:
            return n
        ans=1#2^0
        while ans<=n:
            ans*=2
        return ans
        

        