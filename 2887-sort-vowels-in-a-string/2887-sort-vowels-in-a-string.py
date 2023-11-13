class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        for i, c in enumerate(s):
            if c in 'aeiou' or c in 'AEIOU':
                vowels.append(c)
        
        vowels.sort()
        print(vowels)
        
        for i, c in enumerate(s):
            if c in 'aeiou' or c in 'AEIOU':
                s = s[:i]+vowels.pop(0)+s[i+1:]
        
        return s