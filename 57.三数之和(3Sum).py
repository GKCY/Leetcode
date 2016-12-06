'''
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

注意事项

在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。

您在真实的面试中是否遇到过这个题？ Yes
样例
如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

(-1, 0, 1)

(-1, -1, 2)
'''



class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        length = len(numbers)
        numbers.sort()
        for i in range(0, length - 2):
            if i and numbers[i] == numbers[i-1]:
                    continue
            left = i + 1
            right = length - 1 
            target = -numbers[i]
            while left < right:
                if numbers[left] + numbers[right] == target:
                    res.append([numbers[i], numbers[left], numbers[right]])
                    left += 1 
                    right -= 1
                    while numbers[left] == numbers[left-1] and left < right:
                        left += 1
                    while numbers[right] == numbers[right+1] and left < right:
                        right -= 1
                elif numbers[left] + numbers[right] < target:
                    left += 1 
                else:
                    right -= 1 
        return res
