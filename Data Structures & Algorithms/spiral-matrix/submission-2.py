class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        count = len(matrix) *len(matrix[0])
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        start = 0

        while count > 0:
            while count > 0 and j < m-1 and (i== start):
                res.append(matrix[i][j])
                j += 1
                count -=1 

            
            while count > 0 and i < n-1 and (j==m-1):
                
                res.append(matrix[i][j])
                i += 1
                count -=1            
            
            while count > 0 and j >= start and (i == n-1):
                
                res.append(matrix[i][j])
                j -= 1
                count -=1 

            j += 1
            i-=1
            
            while count > 0 and i >= start+1 and (j == start):
                
                res.append(matrix[i][j])
                i -= 1
                count -=1 
            
            
            i +=1
            j +=1
            m -= 1
            n -= 1
            start += 1
            

        return res




        