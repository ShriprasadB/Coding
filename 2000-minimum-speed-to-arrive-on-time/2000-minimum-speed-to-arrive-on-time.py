class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right, min_speed = 1, 1000000000, float('inf')

        while left <= right:
            mid = (left + right)//2

            total = 0
            for i, d in enumerate(dist):
                if i == len(dist) - 1:
                    total += d/mid
                else:
                    total += ceil(d/mid)
                
            if total > hour:
                left = mid + 1
            else:
                right = mid - 1
                min_speed = min(min_speed, mid)

        return min_speed if min_speed != float('inf') else -1