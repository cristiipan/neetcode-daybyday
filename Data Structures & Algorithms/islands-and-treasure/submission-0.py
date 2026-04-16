from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 2147483647:
                    continue
                grid[row][col] = grid[r][c] + 1
                queue.append((row, col))    # 这一步要放在确认格子是否合法之后

        # 不需要return任何东西因为是in place的修改