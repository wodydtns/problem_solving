def solution(n):
    def is_valid(num, row, col):
        # 현재 위치에 num이 들어갈 수 있는지 검사
        return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

    def in_row(num, row):
        # 해당 행에 num이 있는지 확인
        return num in board[row]

    def in_col(num, col):
        # 해당 열에 num이 있는지 확인하는 함수
        return num in (board[i][col] for i in range(9))

    def in_box(num, row, col):
        # 현재 위치의 3 x 3 박스에 num이 있는지 확인
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

    return results


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
