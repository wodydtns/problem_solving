def solution(dirs):
    dx, dy = 0, 0
    my_set = set()
    my_list = []
    for i in range(len(dirs)):
        if dirs[i] == "U" and dy < 5:
            new_dy = dy + 1
            new_dx = dx
        elif dirs[i] == "D" and dy > -5:
            new_dy = dy - 1
            new_dx = dx
        elif dirs[i] == "R" and dx < 5:
            new_dx = dx + 1
            new_dy = dy
        elif dirs[i] == "L" and dx > -5:
            new_dx = dx - 1
            new_dy = dy
        else:
            new_dx, new_dy = dx, dy  # 명령이 잘못된 경우 위치 변경 없음

        # 이동한 경로 저장 (출발점과 도착점으로 경로를 유일하게 정의)
        if ((dx, dy), (new_dx, new_dy)) not in my_set and (
            (new_dx, new_dy),
            (dx, dy),
        ) not in my_set:
            my_set.add(((dx, dy), (new_dx, new_dy)))

        # 현재 위치 업데이트
        dx, dy = new_dx, new_dy

        print(f"inum: {i}")
        print(f"x: {dx}")
        print(f"y: {dy}")
        my_list.append((dx, dy))
        print(my_list)

    # 중복 경로를 제외한 경로의 수 반환
    answer = len(my_set)
    print(answer)
    return answer


"""
dirs = ["U", "L", "U", "R", "R", "D", "L", "L", "U"]
solution(dirs)


def solution(dirs):
    x, y = 0, 0
    visited = set()
    directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    for direction in dirs:
        nx, ny = x + directions[direction][0], y + directions[direction][1]

        # 좌표가 -5에서 5 사이를 벗어나지 않도록 조건 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    # visited에 저장된 이동 경로의 개수를 정답으로 반환
    answer = len(visited) // 2
    return answer


dirs = ["U", "L", "U", "R", "R", "D", "L", "L", "U"]
print(solution(dirs))  # 예상 출력: 7
"""
