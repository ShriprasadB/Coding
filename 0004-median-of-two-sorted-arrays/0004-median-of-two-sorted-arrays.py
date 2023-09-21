class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total//2
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        
        while True:
            i = (l + r)//2
            j =  half - i - 2
            leftA = nums1[i] if i >= 0 else -float("inf")
            rightA = nums1[i + 1] if i + 1 < len(nums1) else float("inf")
            leftB = nums2[j] if j >= 0 else -float("inf")
            rightB = nums2[j + 1] if j + 1 < len(nums2) else float("inf")
            
            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB))/2

            elif leftA < rightB:
                l = i + 1
            else:
                r = i - 1