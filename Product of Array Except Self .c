//Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

//Solve it without division and in O(n).

//For example, given [1,2,3,4], return [24,12,8,6].


/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* res = (int *)malloc(sizeof(int)*numsSize);
    int before,after;
    before = 1;
    after = 1;
    for(int i = 0;i < numsSize;i++)
    {
        res[i] = before;
        before *= nums[i];
    }
    for(int i = numsSize - 1;i >= 0;i--)
    {
        res[i] *= after;
        after *= nums[i];
    }
    return res;
}
