"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Given strs = ["lint","code","love","you"]
string encoded_string = encode(strs)

return `["lint","code","love","you"]｀ when you call decode(encoded_string)
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ans = ""
        for s in strs:
            for ch in s:
                if ch == ':':
                    ans += '::'
                else:
                    ans += ch
            ans += ':;'
        return ans

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        res = []
        ans = ""
        i = 0
        while i < len(strs):
            if strs[i] == ':':
                if strs[i + 1] == ':':
                    ans += ':'
                    i += 2
                elif strs[i + 1] == ';':
                    res.append(ans)
                    ans = ""
                    i += 2
            else:
                ans += strs[i]
                i += 1
        return res