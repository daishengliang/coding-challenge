"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for ch in t:
            if ch not in dic:
                return ch
            else:
                dic[ch] -= 1
                if dic[ch] == 0:
                    dic.pop(ch)
        for last in dic:
            return last

class Solution2(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        if len(c1) < len(c2):
            c1, c2 = c2, c1
        for key in c1:
            if c1[key] - c2[key] != 0:
                return key