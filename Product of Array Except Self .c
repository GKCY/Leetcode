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
