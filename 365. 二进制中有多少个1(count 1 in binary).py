#计算在一个 32 位的整数的二进制表式中有多少个 1.

class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while num != 0:
            num = num & (num - 1)
            count += 1
        return count
