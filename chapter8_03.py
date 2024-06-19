"""
def solution(participant, completion):
    result_dict = {}
    for i in participant:
        if result_dict.get(i) == None:
            result_dict[i] = 1
        else:
            result_dict[i] += 1
    print(result_dict)
    for j in completion:
        if result_dict.get(j) > 0:
            result_dict[j] -= 1
            if result_dict.get(j) == 0:
                del result_dict[j]

    return print("".join(result_dict))

    """


def solution(participant, completion):
    dic = {}

    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    for c in completion:
        dic[c] -= 1

    for key in dic.keys():
        if dic[key] > 0:
            return key


# case 1
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# case 2
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

# case 3
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "mislav", "ana"]
solution(participant, completion)
