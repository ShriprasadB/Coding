class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        max_time = 0
        queue = [(grid[0][0], 0, 0)]
        visited = set([(0,0)])
                
        while True:
            
            time, x, y = heapq.heappop(queue)
            max_time = max(max_time, time)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return max_time
            
            if x-1 >= 0 and (x-1 , y) not in visited:
                visited.add((x-1,y))
                heapq.heappush(queue, (grid[x-1][y], x-1, y))
                            
            if x+1 <len(grid) and (x+1, y) not in visited:
                visited.add((x+1,y))
                heapq.heappush(queue, (grid[x+1][y], x+1, y))
            
            if y-1 >= 0 and (x, y-1) not in visited:
                visited.add((x,y-1))
                heapq.heappush(queue, (grid[x][y-1], x, y-1))
            
            if y+1 < len(grid[0])  and (x, y+1) not in visited:
                visited.add((x,y+1))
                heapq.heappush(queue, (grid[x][y+1], x, y+1))