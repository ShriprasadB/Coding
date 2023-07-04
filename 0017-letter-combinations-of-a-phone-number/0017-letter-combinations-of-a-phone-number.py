class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        if digits == "":
            return res
         
        dict1 = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
        
        
        letter_string = dict1[int(digits[0])]   
        
        if len(digits) > 1:
            sub_output = self.letterCombinations(digits[1:])

            for c in letter_string:
                for output in sub_output:
                    res.append(c + output)
            
            return res
        
        else:
            return [c for c in letter_string]