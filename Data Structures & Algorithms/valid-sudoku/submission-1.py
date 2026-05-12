import collections
from typing import List 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        colums = defaultdict(set)
        sqaure = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if (val in rows[r] or
                    val in colums[c] or
                    val in sqaure[(r//3,c//3)]):
                    return False


                rows[r].add(val)
                colums[c].add(val)
                sqaure[(r//3,c//3)].add(val)
                    
        return True 
                    




        