//Given an array of integers, every element appears three times except for one. Find that single one.


//解法一
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int i = 0;i < 32;++i)
        {
            int sum = 0;
            for(int j = 0;j < nums.size();++j)
                sum += (nums[j]>>i)&1;
            res |= (sum % 3)<<i;
        }
        return res;
    }
};


//此解法还有改进空间，待以后研究位运算的时候再来思考。
