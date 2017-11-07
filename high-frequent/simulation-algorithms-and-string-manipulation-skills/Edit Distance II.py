"""
Given two strings S and T, determine if they are both one edit distance apart.

Example
Given s = "aDb", t = "adb"
return true
"""
class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if they are both one edit distance apart or false
    def isOneEditDistance(self, s, t):
        # Write your code here
        if len(s) > len(t):
            s, t = t, s
            
        diff = len(t) - len(s)
        if diff > 1:
            return False
            
        if diff == 1:
            i = 0
            while i < len(s):
                if s[i] != t[i]:
                    return s[i:] == t[i + 1:]
                i += 1
        if diff == 0:
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
            return cnt == 1
        return True
            
                
