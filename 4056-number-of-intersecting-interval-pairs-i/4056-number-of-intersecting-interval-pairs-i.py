class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res=sorted(intervals, key=lambda x: x[0])
        total=0
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                # if i==j:
                #     continue
                if res[i][0] <= res[j][1] and res[j][0] <= res[i][1]:
                    total+=1
        return total

        