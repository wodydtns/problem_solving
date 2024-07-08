def solution(n):
    results = []

    def backtrack(sum, selected_nums, start):
        if sum == 10:
            results.append(selected_nums)
            return results

        for i in range(start, n + 1):
            if sum + i <= 10:
                backtrack(sum + i, selected_nums + [i], i + 1)

    backtrack(0, [], 1)
    print(results)
    return results


# n = 5
# n = 2
n = 7
solution(n)
