class Solution:
    def minDeletions(self, s: str) -> int:
        
        dict1 = {}
        count_set = set()
        
        for letter in s:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        
        res = 0
        
        for k, v in dict1.items():
            if v not in count_set:
                count_set.add(v)
            else:
                while v > 0 and v in count_set:
                    res += 1
                    v -= 1
                count_set.add(v)
        
        return res