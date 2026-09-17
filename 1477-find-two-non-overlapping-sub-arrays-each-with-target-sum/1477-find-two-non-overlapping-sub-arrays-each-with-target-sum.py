class Solution(object):
    def minSumOfLengths(self, arr, target):
        i = 0
        currsum = 0
        best = float('inf')
        res = float('inf')
        n = len(arr)
        minLenidx = [float('inf')] * n

        for j in range(n):
            currsum += arr[j]

            while currsum > target:
                currsum -= arr[i]
                i += 1

            if currsum == target:
                l = j - i + 1

                if i > 0 and minLenidx[i - 1] != float('inf'):
                    res = min(res, l + minLenidx[i - 1])

                best = min(best, l)

            minLenidx[j] = best

        return -1 if res == float('inf') else res