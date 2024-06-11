def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            print(f"pop {stack}")
        else:
            stack.append(c)
            print(f"append {stack}")

    return int(not stack)


s = "baabaa"
solution(s)
