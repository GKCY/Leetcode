'''
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

Challenge 
O(m+n) time and O(1) extra space
'''

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        i = row - 1
        j = 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                i -= 1
                j += 1
                count += 1
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return count
                
                
