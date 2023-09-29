class Solution:
    def maxChunksToSorted(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if len(stack) == 0 or stack[-1] <= n:
                stack.append(n)
            else:
                max_ = stack[-1]
                while stack and stack[-1] > n:
                    stack.pop()
                stack.append(max_)

        return len(stack)