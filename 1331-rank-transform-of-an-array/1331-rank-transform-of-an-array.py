class Solution(object):
    def arrayRankTransform(self, arr):
        rank={}
        for i,el in enumerate(sorted(set(arr))):
            rank[el]=i+1
        #print(rank)
        return [rank[el]for el in arr]


        