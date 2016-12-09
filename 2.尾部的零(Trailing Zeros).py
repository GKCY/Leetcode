#Write an algorithm which computes the number of trailing zeros in n factorial.


class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        sum = 0
        while n:
            n /= 5
            sum += n
        return sum
        
            
