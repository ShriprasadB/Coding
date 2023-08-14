class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start, res, n = [], [], len(intervals)
        
        for i, (x, y) in enumerate(intervals):
            start.append([x, i])
        
        start.sort()

        for i in range(n):
            l, r = 0, n - 1
            index = -1
            while l <= r:
                m = (l + r)//2

                if start[m][0] >= intervals[i][1]:
                    index = start[m][1]
                    r = m - 1
                else:
                    l = m + 1
            
            res.append(index)
        
        return res