//给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

//不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
 
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if(nums.length < 2)
            return nums.length;
        int id = 1;
        for (int i = 1; i < nums.length; i++) 
        {
            if(nums[i] != nums[i-1])
                nums[id++] = nums[i];
        }
        return id;
        
    }
}  
