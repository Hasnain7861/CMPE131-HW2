def swap_list(aList):

    if len(aList) == 0:
        return None  
    else:
        number = int((len(aList) - 1) / 2)
        size = len(aList) - 1

        temp = aList[number]
        aList[number] = aList[size]
        aList[size] = temp 
        # aList[number], aList[size] = aList[size], aList[number]  

    return aList       

hey = [1, True, 9, "‘Hi’", 3]

print(swap_list(hey))