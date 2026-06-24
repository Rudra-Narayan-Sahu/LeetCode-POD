class Solution(object):
    def generateMatrix(self, n):
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        top,left = 0, 0
        bottom,right=n-1,n-1
        number=1
        while left<=right and top<=bottom:
            #left-->right
            for i in range(left,right+1):
                matrix[top][i]=number
                number+=1
            top+=1
            #top->bottom
            for j in range(top,bottom+1):
                matrix[j][right]=number
                number+=1
            right-=1
            #right-->left
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=number
                    number+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=number
                    number+=1
                left+=1
        return matrix