"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        left, right = 0, len(s) - 1
        sl = list(s)
        while 1:
            while left < len(s) and sl[left].lower() not in VOWELS:
                left += 1
            while right >= 0 and sl[right].lower() not in VOWELS:
                right -= 1
            if left > right:
                break
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -=1
        return ''.join(sl)