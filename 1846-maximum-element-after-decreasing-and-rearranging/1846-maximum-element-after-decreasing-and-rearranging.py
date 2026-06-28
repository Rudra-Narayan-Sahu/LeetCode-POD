class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0]=1
        for k in range(1,len(arr)):
            if arr[k]>arr[k-1]+1:
                arr[k]=arr[k-1]+1
        return arr[-1]
