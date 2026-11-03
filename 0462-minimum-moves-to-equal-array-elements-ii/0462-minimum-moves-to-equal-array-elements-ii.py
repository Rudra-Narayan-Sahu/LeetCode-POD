class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        md=nums[len(nums)//2]
        moves=0
        for el in nums:
            moves+=abs(el-md)
        return moves