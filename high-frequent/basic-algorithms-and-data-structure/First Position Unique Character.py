"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


Example
Given s = "lintcode", return 0.

Given s = "lovelintcode", return 2.
"""
class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1