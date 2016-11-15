'''
返回两个数组的交
样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].
'''


class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        return list(set(nums1) & set(nums2))
