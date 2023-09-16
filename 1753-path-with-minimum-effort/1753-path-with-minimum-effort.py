class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        efforts = [[float('inf')]*col for _ in range(row)]
        efforts[0][0] = 0
        visited = set()
        pq = [(0, 0, 0)]  # difference, x, y
        
        while pq:
            max_e, x, y = heapq.heappop(pq)
            visited.add((x,y))
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y)not in visited:
                    max_diff = max(abs(heights[new_x][new_y] - heights[x][y]), max_e)
                    if max_diff < efforts[new_x][new_y]:
                        efforts[new_x][new_y] = max_diff
                        heapq.heappush(pq, (max_diff, new_x, new_y))

        return efforts[-1][-1]