from collections import deque


def solution(n, k):
    # 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1, n + 1))

    # deque에 하나의 요소가 남을 때까지
    while len(queue) > 1:
        for _ in range(k - 1):
            # k 번째 요소를 찾기 위해 앞에서부터 제거하고 뒤에 추가
            queue.append(queue.popleft())

            queue.popleft()
    print(queue[0])
    return queue[0]


print(solution(5, 2))
