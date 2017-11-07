"""
Given an integer, convert it to a roman numeral.

The number is guaranteed to be within the range from 1 to 3999.

Clarification
What is Roman Numeral?

https://en.wikipedia.org/wiki/Roman_numerals
https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
http://baike.baidu.com/view/42061.htm
Example
4 -> IV

12 -> XII

21 -> XXI

99 -> XCIX

more examples at: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
"""
class Solution:
    """
    @param: n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return M[n / 1000] + C[(n / 100) % 10] + X[(n / 10) % 10] + I[n % 10]
