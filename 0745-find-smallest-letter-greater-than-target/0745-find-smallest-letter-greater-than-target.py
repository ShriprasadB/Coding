class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
    
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                while mid + 1 < len(letters) and letters[mid] == letters[mid + 1]:
                    mid += 1
                
                return letters[mid + 1] if mid + 1 != len(letters) else letters[0]
            if letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]