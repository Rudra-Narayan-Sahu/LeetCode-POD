class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=float('inf')
        hasOdd=False
        for el in nums1:
            if el<mn:
                mn=el
            if el&1:
                hasOdd=True
        if mn%2!=0:
            return True
        return not hasOdd