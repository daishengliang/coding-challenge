"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n < 1:
            return False
        return (math.log10(n)/math.log10(3)) % 1 == 0