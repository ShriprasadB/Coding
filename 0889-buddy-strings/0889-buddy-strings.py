class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            frequency = [0]*26
            for c in s:
                frequency[ord(c) - ord('a')] += 1
                if frequency[ord(c) - ord('a')] == 2:
                    return True
            
            return False

        first_idx, second_idx = -1, -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if first_idx == -1:
                    first_idx = i
                elif second_idx == -1:
                    second_idx = i
                else:
                    return False
        
        if second_idx == -1:
            return False
        
        return s[first_idx] == goal[second_idx] and s[second_idx] == goal[first_idx]