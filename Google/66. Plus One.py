"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        reverse = list(reversed(digits))
        for i in range(len(digits)):
            
            if reverse[i] + flag == 10:
                reverse[i] = 0
                flag = 1
            else:
                reverse[i] += flag
                flag = 0
        if flag == 1:
            reverse.append(1)
        return list(reversed(reverse))