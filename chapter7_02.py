import math


def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    # 각 작업의 배포 가능일 계산
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    # 배포될 작업의 수 카운트
    count = 0

    # 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일
    max_day = days_left[0]

    for i in range(n):
        if days_left[i] <= max_day:
            count += 1
        # 배포 예정일이 기준 배포일보다 느리면
        else:
            answer.append(count)
            count = 1
            max_day = days_left[i]
    answer.append(count)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)
