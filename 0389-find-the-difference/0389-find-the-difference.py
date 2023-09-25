class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1 = {}

        for c in s:
            if c not in dict1:
                dict1[c] = 1
            else:
                dict1[c] += 1
        
        result = ""
        for c in t:
            if c in dict1:
                dict1[c] -= 1
                if dict1[c] == 0:
                    dict1.pop(c)
            else:
                result += c
        
        return result