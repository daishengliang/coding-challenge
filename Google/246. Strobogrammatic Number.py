"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        
        if len(num) == 1 and num[0] not in d:
            return False
            
        i, j = 0, len(num) - 1
        while 1:
            if i>j:
                break
            if i == j:
                return num[i] in ['0', '1', '8']
            if num[i] in d and d[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        return True