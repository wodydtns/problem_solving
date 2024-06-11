def solution(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result.append(arr[i] + arr[j])
    result = sorted(list(set(result)))
    print(result)


numbers = [5, 0, 2, 7]
solution(numbers)
