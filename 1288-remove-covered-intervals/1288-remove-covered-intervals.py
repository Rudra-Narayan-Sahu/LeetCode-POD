class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #Make a nested loop for the brute force
        intervals.sort(key=lambda x: (x[0], -x[1]))#sort based on start point
        co=0
        max_end=0
        for st,end in intervals:
            if end>max_end:
                co+=1
                max_end=end
        return co


