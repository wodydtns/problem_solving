def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    rollback_cmd = []
    for ch in cmd:
        if k <= 0:
            k = 1
        elif k > n:
            k = n
        if len(ch) > 1:
            direction = ch.split()[0]
            count = ch.split()[1]
            if direction == "U":
                k -= int(count)
            else:
                k += int(count)
        elif ch == "Z":
            pop_idx = rollback_cmd.pop()
            answer[pop_idx] = "O"
        else:
            answer[k] = "X"
            n -= 1
            rollback_cmd.append(k)
    print("".join(answer))


# case 1
"""
n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
"""
n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
solution(n, k, cmd)
