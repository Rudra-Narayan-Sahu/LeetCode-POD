class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=min(nums1)
        if mn%2!=0:
            return True
        for el in nums1:
            if el%2!=0:
                return False
        return True
