def reverse_list(aList):
    newList = []
    for a in range(len(aList) - 1, -1, -1):
        newList.append(aList[a])
    return newList

# print(reverse_list([1,2,3,4]))