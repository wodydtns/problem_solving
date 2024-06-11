def solution(answers):
    # 수포자 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    # 수포자들의 점수를 저장할 리스트
    scores = [0] * 3
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    max_score = max(scores)
    highest_scores = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i)


answer = [1, 3, 2, 4, 2]
solution(answer)
