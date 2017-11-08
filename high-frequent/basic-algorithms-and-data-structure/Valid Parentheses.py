"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Example
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        stack = []
        dic = {'(':')', '{': '}', '[' : ']'}
        for c in s:
            if c == '(' or c == '{' or c =='[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if dic[stack.pop()] != c:
                    return False
        return not stack