class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

            for i in range(len(board)):
                seen = set()
                for j in range(len(board)):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

            for i in range(len(board)):
                seen = set()
                for j in range(len(board)):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

            for box_r in range(0, 9, 3):
                for box_c in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):

                            row_index = box_r + i
                            col_index = box_c + j

                            current_value = board[row_index][col_index]

                            if current_value == ".":
                                continue
                            if current_value in seen:
                                return False
                            seen.add(current_value)

            return True