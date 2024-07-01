def solution(n, words):
    # 이미 사용한 단어를 저장하는 set
    used_words = set()

    # 이전 단어의 마지막 글자
    prev_word = words[0][0]

    for i, word in enumerate(words):
        # 이미 사용한 단어이거나 첫 글자가 이전 단어와 일치하지 않으면
        if word in used_words or word[0] != prev_word:
            # 탈락하는 사람의 번호와 차례를 교환
            return [(i % n) + 1, (i // n) + 1]
        # 사용한 단어로 추가
        used_words.add(word)

        # 이전 단어의 마지막 글자 업데이트
        prev_word = word[-1]
    # 모두 통과 시
    return [0, 0]


# case 1
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# case 2
"""
n = 5
words = [
    "hello",
    "observe",
    "effect",
    "take",
    "either",
    "recognize",
    "encourage",
    "ensure",
    "establish",
    "hang",
    "gather",
    "refer",
    "reference",
    "estimate",
    "executive",
]
"""
solution(n, words)
