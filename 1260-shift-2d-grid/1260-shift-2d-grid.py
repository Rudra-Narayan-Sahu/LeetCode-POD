class Solution(object):
    def shiftGrid(self, grid, k):
        f=[el for row in grid for el in row]
        k%=len(f)
        res=f[-k:]+f[:-k]
        matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        idx=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                matrix[i][j]=res[idx]
                idx+=1
        return matrix

        