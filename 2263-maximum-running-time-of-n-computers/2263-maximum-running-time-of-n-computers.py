class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        start, end = 0, sum(batteries)
        
        def isPossible(average):
            duration = 0

            for battery in batteries:
                if battery < average:
                    duration += battery
                else:
                    duration += average
            
            return duration >= n * average
        
        while start <= end:
            average = (start + end)//2

            if isPossible(average):
                answer = average
                start = average + 1
            else:
                end = average - 1

        return answer

