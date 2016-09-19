/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int part = 0;
    *returnSize = 2;
    for(int i = 0;i < numsSize;i++)
        part ^= nums[i];
    part &= -part;
    int* res = (int *)malloc(sizeof(int) * 2);
    res[0] = 0;
    res[1] = 0;
    for(int i=0;i<numsSize;i++)
    {
        if((nums[i] & part) == 0)
            res[0] ^= nums[i];
        else
            res[1] ^= nums[i];
    }
    return res;
    
}
