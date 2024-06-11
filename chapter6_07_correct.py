def solution(n, k, cmd):

    # 삭제된 행의 인덱스를 저장하는 리스트
    deleted = []

    # 링크드리스트에서 각 행 위 아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    # 현재 위치를 나타내는 인덱스
    k += 1

    # 주어진 cmd 리스트를 하나씩 처리
    for cmd_i in cmd:
        # 현재 위치를 삭제하고 그다음 위치로 이동
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        # U 또는 D를 사용해 현재 위치를 위아래로 이동
        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
        # 삭제된 행의 위치를 'X'를, 그렇지 않은 행의 위치를 'O'를 포함하는 문자열 반환
        answer = ["O"] * n
        for i in deleted:
            answer[i - 1] = "X"
        return "".join(answer)
