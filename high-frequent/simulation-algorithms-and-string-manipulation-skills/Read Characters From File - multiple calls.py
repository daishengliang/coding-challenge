"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

 Notice

The read function may be called multiple times.

"""

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:
    
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.buf = [None] * 4
        
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.head == self.tail:
                self.head = 0
                self.tail = Reader.read4(self.buf)
                if self.tail == 0:
                    break
            buf[i] = self.buf[self.head]
            self.head += 1
            i += 1
        return i