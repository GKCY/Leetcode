#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def slopeCalc(self, pointA, pointB):
        if pointA.x == pointB.x:
            return None
        x = pointA.x - pointB.x
        y = pointA.y - pointB.y
        res = 1.0 * y / x
        return res
    
    def isEqual(self, pointA, pointB):
        return pointA.x == pointB.x and pointA.y == pointB.y

    def maxPoints(self, points):
        # Write your code here
        ans = 0
        size = len(points)
        for x in range(size):
            k_dict = {}
            same = 0
            for y in range(x+1, size):
                if self.isEqual(points[x], points[y]):
                    same += 1
                else:
                    k = self.slopeCalc(points[x], points[y])
                    if k_dict.get(k) is None:
                        k_dict[k] = 1
                    else:
                        k_dict[k] += 1
            val = 0
            if len(k_dict):
                val = max(k_dict.values())
            ans = max(ans, val+1+same)
        return ans    
            
                
                
