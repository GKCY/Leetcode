#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. click to show follow up. 
#Follow up: Did you use extra space? A straight forward solution using O(mn) space is probably a bad idea. A simple improvement
#uses O(m + n) space, but still not the best solution. Could you devise a constant space solution?

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
                    
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0
