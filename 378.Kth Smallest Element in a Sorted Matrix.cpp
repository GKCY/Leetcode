//Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

//Note that it is the kth smallest element in the sorted order, not the kth distinct element.

//Example:

//matrix = [
//   [ 1,  5,  9],
//   [10, 11, 13],
//   [12, 13, 15]
//],
//k = 8,

//return 13.
//Note: 
//You may assume k is always valid, 1 ≤ k ≤ n2.

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> res;
        for(int i = 0 ;i < matrix.size();i++)
            for(int j = 0;j <matrix.size();j++)
                res.push_back(matrix[i][j]);
        sort(res.begin(),res.end());
        return res[k-1];
    }
};

//使用优先队列的解法参见python文件
