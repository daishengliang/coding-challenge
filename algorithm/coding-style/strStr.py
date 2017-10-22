"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure your confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

"""
class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        #if not source or not target: # test case: ['', ''] will return 0
        if source is None or target is None:    
            return -1
        for i in range(len(source) - len(target) + 1):
            j = 0
            while j < len(target):
                if source[i + j] != target[j]:
                    break
                else:
                    j += 1
            if j == len(target):
                return i
        return -1