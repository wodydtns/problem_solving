from collections import deque


def solution(card1, card2, goal):
    answer = []
    card1_queue = deque(card1)
    card2_queue = deque(card2)
    goal = deque(goal)

    while goal:
        if card1_queue and card1_queue[0]:
            card1_queue.popleft()
            goal.popleft()
        elif card2_queue and card2_queue[0]:
            card2_queue.popleft()
            goal.popleft()
        else:
            break
    return "Yes" if not goal else "No"


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
solution(cards1, cards2, goal)
