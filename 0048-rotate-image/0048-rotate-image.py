class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for i in range(len(matrix)):
            j,k=0,len(matrix)-1
            while j<=k:
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][k]
                matrix[i][k]=temp
                j+=1
                k-=1
        return matrix


        