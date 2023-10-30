class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        n = len(arr)
        arr[-1] = -1
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_
            max_ = max(max_, temp)

        return arr