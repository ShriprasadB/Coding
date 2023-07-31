class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        def palindrome(left, right):
            nonlocal res
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
        
        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i + 1)
        
        return res
            
        