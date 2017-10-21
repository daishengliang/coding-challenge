"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        Basic idea is:
        iff s with odd characters, only one character is allowed to appear odd times.
        iff s with even characters, each character should appear even times. 

        :type s: str
        :rtype: bool
        """
        from collections import Counter
        cnt = Counter(s)
        
        numOfEven = 0
        numOfOdd = 0
        for i in cnt:
            if cnt[i] % 2 == 0:
                numOfEven += 1
            else:
                numOfOdd += 1
        if numOfOdd <= 1:
            return True
        return False
            