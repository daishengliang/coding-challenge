"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        ans = ""
        carry = 0
        
        while l1 >= 0 or l2 >= 0:
            _sum = carry
            if l1 >= 0:
                _sum += ord(num1[l1]) - ord('0')
                l1 -= 1
            if l2 >= 0:
                _sum += ord(num2[l2]) - ord('0')
                l2 -= 1
            ans = str(_sum % 10) + ans
            carry = _sum / 10
        if carry > 0:
            ans = str(carry) + ans
        return ans