"""
def solution(num):
    answer = 0
    answer = format(num, "b")
    print(answer)


num = 12345
solution(num)
"""


def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2
    binary = ""
    while stack:
        binary += stack.pop()
    return binary
