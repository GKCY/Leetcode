//Given two arrays, write a function to compute their intersection.

//Example:
//Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

//Note:
//1.Each element in the result should appear as many times as it shows in both arrays.
//2.The result can be in any order.

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> dict;
        vector<int> res;
        for(int i = 0;i < nums1.size();i++)
            dict[nums1[i]]++;
        for(int i = 0;i < nums2.size();i++)
            if(--dict[nums2[i]] >= 0)
                res.push_back(nums2[i]);
                
        return res;
    }
};
