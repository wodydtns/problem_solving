def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = [0]
    for i in range(1, n):
        # 이전 가격보다 떨어짐
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어졌으므로 이전 가격의 기간 계산
            j = stack.pop()
            print(f" j: {j}")
            answer[j] = i - j
            print(f" answer[i] : {answer[i]}")
        stack.append(i)
    # 스택에 남아있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer


prices = [1, 2, 3, 2, 3]
solution(prices)
