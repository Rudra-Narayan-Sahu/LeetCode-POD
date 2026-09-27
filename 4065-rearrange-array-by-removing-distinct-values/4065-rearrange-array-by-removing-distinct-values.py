class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map=Counter(nums)
        ans=[]
        while map:
            dis_el=sorted(map.keys())
            for num in dis_el:
                ans.append(num)
                map[num]-=1
                if map[num]==0:
                    del map[num]
        return ans
        