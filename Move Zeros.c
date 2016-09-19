void moveZeroes(int* nums, int numsSize) {
    int pointer = 0;
    for(int i = 0;i<numsSize;i++)
    {
        if(nums[i] != 0)
        {
            int temp = nums[i];
            nums[i] = nums[pointer];
            nums[pointer] = temp;
            pointer++;
        }
    }
    return nums;
}
