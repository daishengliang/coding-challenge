"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 40,000.

The order of output does not matter.

Example
Given s = "cbaebabacd" p = "abc"

return [0, 6]

The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

class Solution:
    # @param {string} s a string
    # @param {string} p a non-empty string
    # @return {int[]} a list of index
    def findAnagrams(self, s, p):
        # Write your code here
        ans = []
        sum = [0 for _ in range(30)]
        
        for i in range(len(p)):
            sum[ord(p[i]) - ord('a')] += 1
            
        start = 0
        end = 0
        matched = 0
        while end < len(s):
            if sum[ord(s[end]) - ord('a')] >= 1:
                matched += 1
            sum[ord(s[end]) - ord('a')] -= 1
            end += 1
            if matched == len(p):
                ans.append(start)
            if end - start == len(p):
                sum[ord(s[start]) - ord('a')] += 1
                if sum[ord(s[start]) - ord('a')] >= 1:
                    matched -= 1
                start += 1
        return ans