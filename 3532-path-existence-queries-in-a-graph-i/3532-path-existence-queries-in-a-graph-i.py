class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp=[0]*n
        
        for i in range(1,len(nums)):
            dif=abs(nums[i]-nums[i-1])
            if dif<=maxDiff:
                comp[i]=comp[i-1]
            else:
                comp[i]=i
        ans=[]
        for st,end in queries:
            if comp[st]==comp[end]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
