"""
Given a roman numeral, convert it to an integer.

The answer is guaranteed to be within the range from 1 to 3999.


Clarification
What is Roman Numeral?

https://en.wikipedia.org/wiki/Roman_numerals
https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
http://baike.baidu.com/view/42061.htm
Example
IV -> 4

XII -> 12

XXI -> 21

XCIX -> 99
"""
class Solution:
    """
    @param: s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        if not s:
            return 0
        to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = to_int[s[0]]
        for i in range(1, len(s)):
            ans += to_int[s[i]]
            if to_int[s[i - 1]] < to_int[s[i]]:
                ans -= 2 * to_int[s[i - 1]]
        return ans
        
