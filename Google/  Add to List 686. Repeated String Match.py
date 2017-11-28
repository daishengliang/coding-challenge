"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

"""

import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m = len(A)
        n = len(B)
        q = int(math.ceil(n * 1.0 / m))
        s = q * A
        if s.find(B) >= 0:
            return q
        s += A
        if s.find(B) >= 0:
            return q + 1
        return -1