"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

 Notice

Assume the length of given string will not exceed 1010.


Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    """
    @param: s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0
            
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        ans = 0
        odd = False
        for key in dic:
            if dic[key] % 2 == 0:
                ans += dic[key]
            else:
                ans += dic[key] - 1
                odd = True
                
        if odd:
            ans += 1
        return ans