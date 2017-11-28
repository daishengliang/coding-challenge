"""
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '

"""
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.i = 0
        self.cnt = 0
        self.c = ' '
        

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.cnt -= 1
            return self.c
        return ' '
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cnt > 0:
            return True
        if self.i >= len(self.s):
            return False
        self.c = self.s[self.i]
        self.i += 1
        while self.i < len(self.s) and '0' <= self.s[self.i] <= '9':
            self.cnt = self.cnt * 10 + ord(self.s[self.i]) - ord('0')
            self.i += 1
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()