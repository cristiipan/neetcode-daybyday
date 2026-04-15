class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        col = len(board[0])     # 宽度 / 列
        row = len(board)        # 高度 / 行

        if col * row < len(word):
            return False
            
        def backtrack(r, c, index):
            if index == len(word):
                return True
            """
            为什么下面四个关于格子合法的判断直接 return False：
            这里的逻辑是：backtrack(r, c, index) 的含义是"从格子 (r,c) 出发，能否匹配 word[index] 及之后的字符"。
            如果当前格子不合法，说明这条路走不通，直接告诉上一层"不行"。
            其他的可能性不需要在这里查——上一层调用者会负责尝试其他方向！
            """
            if r < 0 or r >= row:
                return False
            if c < 0 or c >= col:
                return False
            # ‘#’ 是我们自己选的一个标记符号，表示"这个格子已经被当前路径使用过了"
            # 在递归之前把 board[r][c] 改成 #，递归结束后再恢复原来的字母——这就是原地标记 + 回溯
            if board[r][c] == "#":
                return False
            if board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            result = (backtrack(r - 1, c, index + 1 ) or backtrack(r, c - 1, index + 1) or backtrack(r + 1, c, index + 1) or backtrack(r, c + 1, index + 1))
            board[r][c] = temp
            return result

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False

        