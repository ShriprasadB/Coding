class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = float("inf")
        final = ""
        for item in strs:
            if len(item) < ans:
                ans = len(item)
                res = item
        for i in range(len(res)):
            count = 0
            for word in strs:
                if word[i] == res[i]:
                    count += 1
            if count == len(strs):
                final += word[i]
            else:
                break
        
      
                
        return final