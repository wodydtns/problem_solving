def solution(board, moves):
    # 각 열에 대한 스택 생성
    lanes = [[] for _ in range(len(board[0]))]

    # board를 역순으로 탐색하며, 각 열의 인형을 lanes에 추가
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])

    # 인형을 담을 bucket을 생성
    bucket = []

    # 사라진 인형의 총 개수를 저장할 변수를 초기화
    answer = 0

    # moves를 순회하면서 각 열에서 인형을 뽑아 bucket에 추가
    for move in moves:
        if lanes[move - 1]:  # 해당 열에 인형이 있는 경우
            doll = lanes[move - 1].pop()

        # 바구니에 인형이 있꼬, 가장 위에 있는 인형과 같은 경우
        if bucket and bucket[-1] == doll:
            bucket.pop()
            answer += 2
        # 바구니에 인형이 없거나, 가장 위에 있는 인형과 다른 경우
        else:
            bucket.append(doll)
    print(answer)
    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]

moves = [1, 5, 3, 5, 1, 2, 1, 3, 4]
# 결과 : 4
solution(board, moves)
