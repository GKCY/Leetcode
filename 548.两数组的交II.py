'''
计算两个数组的交
样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
'''


class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        res = []
        index1 = 0
        index2 = 0
        nums1.sort()
        nums2.sort()
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return res
            
