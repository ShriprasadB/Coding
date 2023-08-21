class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(n):
            if i + 1 == n:
                break
            
            if n % (i+1) == 0:
                substrlen = n // (i + 1)
                if s[:i + 1]*substrlen == s:
                    return True
            else:
                continue
            
        return False
