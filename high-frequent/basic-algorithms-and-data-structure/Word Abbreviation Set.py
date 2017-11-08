"""
An abbreviation of a word follows the form . Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Have you met this question in a real interview? Yes
Example
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") // return false
isUnique("cart") // return true
isUnique("cane") // return false
isUnique("make") // return true
"""

class ValidWordAbbr:

    # @param {str[]} dictionary a list word
    def __init__(self, dictionary):
        # Write your code here
        self.d = collections.defaultdict(set)
        for word in dictionary:
            self.d[self.get_abbr(word)].add(word)


    # @param {string} word a string
    # @return {boolean} true if its abbreviation is unique or false
    def isUnique(self, word):
        # Write your code here
        key = self.get_abbr(word)
        if key not in self.d:
            return True
        ans = self.d[key]
        
        return len(self.d[key]) == 1 and word in self.d[key]
        
    def get_abbr(self, word):
        if len(word) > 2:
            return word[0] + str(len(word) - 2) + word[-1]
        else:
            return word



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)