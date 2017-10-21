"""
https://leetcode.com/problems/longest-absolute-file-path/description/
"""
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen= {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            # if it is a directory
            if '.' not in name:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
            else:
                maxlen = max(maxlen, pathlen[depth] + len(name))
        return maxlen