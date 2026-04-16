from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:     # 记录所有初始的烂橘子
                    queue.append((r, c))

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]     # 这里也可以改成[()] tuples in list节省内存
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()  # we take out a rotten orange
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc     # neighbor's directions
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
            if queue:       # 如果queue不为空 说明这一轮有新感染 那么time+1 如果上面while跑完但是没有新增烂橘子 到这里time就不会+1了
                time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time
    
