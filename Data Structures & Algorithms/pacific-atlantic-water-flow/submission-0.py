from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res_pacific = set()
        res_atlantic = set()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q_pacific = deque()
        q_atlantic = deque()

        for r in range(rows):
            q_pacific.append([r, 0])
            res_pacific.add((r, 0))
        for c in range(cols):
            q_pacific.append([0, c])
            res_pacific.add((0, c))
        while q_pacific:
            row, col = q_pacific.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or heights[nr][nc] < heights[row][col] or (nr, nc) in res_pacific:
                    continue
                q_pacific.append([nr, nc])
                # res_pacific.add([nr, nc])   # 🙅 list 不能哈希
                res_pacific.add((nr, nc))
                
        for r in range(rows):
            q_atlantic.append([r, cols - 1])
            res_atlantic.add((r, cols - 1))
        for c in range(cols):
            q_atlantic.append([rows - 1, c])
            res_atlantic.add((rows -1, c))
        while q_atlantic:
            row, col = q_atlantic.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or heights[nr][nc] < heights[row][col] or (nr, nc) in res_atlantic:
                    continue
                q_atlantic.append([nr, nc])
                res_atlantic.add((nr, nc))
        
        res = []
        for r, c in res_atlantic:
            if (r, c) in res_pacific:
                res.append([r, c])
        return res