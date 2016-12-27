#Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1
        return candidate1 if count1 > count2 else candidate2
