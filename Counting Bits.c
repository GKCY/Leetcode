/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    num = num + 1;
    *returnSize = num;
    int *arry;
    arry = (int *)malloc(sizeof(int)*num);
    arry[0] = 0;
    for(int i=1;i<num;i++)
         arry[i] = arry[i/2] + i%2;
    *returnSize = num;
    return arry;
}
