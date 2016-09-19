/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int left,right;
    left = 0;
    right = numbersSize - 1;
    *returnSize = 2;
    while((numbers[left] + numbers[right]) != target)
    {
        if((numbers[left] + numbers[right]) < target)
            left++;
        else
            right--;
    }
    int *res = malloc(sizeof(int) * 2);
    res[0] = left+1;
    res[1] = right+1;
    return res;
}
