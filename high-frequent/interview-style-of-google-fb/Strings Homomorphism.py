"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

 Notice

You may assume both s and t have the same length.

Example
Given s = "egg", t = "add", return true.

Given s = "foo", t = "bar", return false.

Given s = "paper", t = "title", return true.
"""
class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if the characters in s 
    # can be replaced to get t or false
    def isIsomorphic(self, s, t):
        # Write your code here
        map1 = {}
        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]] = t[i]
            else:
                if map1[s[i]] != t[i]:
                    return False
        map2 = {}
        for i in range(len(t)):
            if t[i] not in map2:
                map2[t[i]] = s[i]
            else:
                if map2[t[i]] != s[i]:
                    return False  
                    
        return True
        
