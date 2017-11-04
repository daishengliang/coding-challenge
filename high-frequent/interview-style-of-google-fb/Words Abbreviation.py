"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
 Notice

Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

Example
Given dict = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
return ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
"""
class Solution:
    # @param {string[]} dict an array of n distinct non-empty strings
    # @return {string[]} an array of minimal possible abbreviations for every word
    
    def wordsAbbreviation(self, words):
        # Write your code here
        self.dic = {}
        self.solve(words, 0)
        return [self.dic[key] for key in words]
        
        
    def solve(self, words, size):
        dic_abbr = collections.defaultdict(list)
        for word in words:
            abbr = self.get_abbr(word, size)
            dic_abbr[abbr].append(word)
        for key, value in dic_abbr.items():
            if len(value) == 1:
                self.dic[value[0]] = key
            else:
                self.solve(value, size + 1)

            
    def get_abbr(self, word, size):
        if len(word) - size <= 3:
            return word
        j = 0
        for _ in range(size + 1, len(word) - 1):
            j += 1
        return word[:size + 1] + str(j) + word[-1]