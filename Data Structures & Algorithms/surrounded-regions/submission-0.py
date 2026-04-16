from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # initialize the queue by adding all Os on the boarder
        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r, 0))    # 这里最好的做法是边界格子加入queue的时候也标记成O1，最后扫描全部格子、整体替换
                board[r][0] = "O1"
            if board[r][cols - 1] == "O":
                queue.append((r, cols - 1))
                board[r][cols - 1] = "O1"
        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "O1"
            if board[rows - 1][c] == "O":
                queue.append((rows - 1, c))
                board[rows - 1][c] = "O1"
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] == "X" or board[nr][nc] == "O1":
                    continue
                board[nr][nc] = "O1"    # we find a new O connected to the safe Os and mark it as O1
                queue.append((nr, nc))  # push it into queue for next round
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "O1":
                    board[r][c] = "O"