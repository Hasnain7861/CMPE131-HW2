def sort_dictionary(aDictionary):
    listOfItems = sorted(aDictionary.items(), key = lambda x: x[1][1])
    listOfNameAndPhoneNumber = []
    for i in listOfItems:
        listOfNameAndPhoneNumber.append((i[0], i[1][0]))
    return listOfNameAndPhoneNumber

# print(sort_dictionary({"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}))
