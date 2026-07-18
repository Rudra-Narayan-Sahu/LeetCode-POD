class Solution(object):
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def findGCD(self, nums):
        small=nums[0]
        big=nums[0]
        for el in nums:
            if el>big:
                big=el
            elif el<small:
                small=el
        return self.gcd(small,big)

        