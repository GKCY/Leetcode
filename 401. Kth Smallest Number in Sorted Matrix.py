#Find the kth smallest number in at row and column sorted matrix.

from heapq import *
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        res = None
        q = [(matrix[0][0], 0, 0)]
        for i in range(k):
            res, i, j = heappop(q)
            if j == 0 and i + 1 < m:
                heappush(q, (matrix[i+1][j], i+1, j))
            if j + 1 < n:
                heappush(q, (matrix[i][j+1], i , j+1))
        return res
