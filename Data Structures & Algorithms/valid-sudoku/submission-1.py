"""
strategy applied here:
Use three hash maps to track seen values across rows, cols, and boxes.
One pass through all 81 cells is sufficient.
"""

from collections import defaultdict
class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
        # in order to fulfill the 3 requirements given out by the question
        # we use 3 dictionary to track all the values came up in the corresponding range
        # each row / each col / each 3x3 box
        # for row and col, index is the key; for box, (i//3, j//3) this tuple is the key
        # we use a set to track all the corresponding values
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j] # we iterate through all 81 positions and track all the values
                if val == ".":      # we skip empty cells (all the ".")
                    continue

                # in order to determine if it's valid, we need to see all 3 sets of constraints:
                # if it already came up in the same row ? / same col ? / same box?
                # if it did, then false
                if (val in rows[i] or 
                    val in cols[j] or 
                    val in box[i // 3, j // 3]):
                    return False
                
                # otherwise, add the val to its row / col / box
                rows[i].add(val)
                cols[j].add(val)
                box[i // 3, j // 3].add(val)
        
        return True