class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        rows=[0]*n
        cols=[0]*m
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i]+=1
                    cols[j]+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (rows[i]>1 or cols[j]>1):
                    count+=1
        return count



