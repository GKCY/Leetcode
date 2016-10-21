//Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
//
//
//Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
//
//
//The largest rectangle is shown in the shaded area, which has area = 10 unit.
//
//For example,
//Given heights = [2,1,5,6,2,3],
//return 10.
//
//由于图片无法显示，给出此题地址
//https://leetcode.com/problems/largest-rectangle-in-histogram/
//此解法对于栈的运用极其巧妙，可以仔细钻研

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if(heights.size() == 0) 
            return 0;
        int res = 0;
        vector<int> tmp = heights;
        tmp.push_back(0);
        
        stack<int> s;
        for(int i = 0; i < tmp.size(); i++)
        {
            if(s.empty() || (!s.empty() && tmp[i] >= tmp[s.top()]))
                s.push(i);
            else
            {
                while(!s.empty() && tmp[s.top()] > tmp[i])
                {
                    int idx = s.top();
                    s.pop();
                    int width = s.empty() ? i : (i - s.top() - 1);
                    res = max(res, tmp[idx] * width);
                }
                s.push(i);
            }
        }
        return res;
    }
};
