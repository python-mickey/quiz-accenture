from itertools import combinations

def FindPossibleList(inputList):
    # all posible list
    list_all = sum([list(map(list, combinations(inputList, i))) for i in range(len(inputList) + 1)], [])
    # all answer list
    list_answer = list_all[len(inputList) + 1:-1]
    return list_answer

print(FindPossibleList(['A', 'B', 'C','D','E','F']))
