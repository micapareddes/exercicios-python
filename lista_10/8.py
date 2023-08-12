def concat_lists(list_one, list_two):
    indOne = 0
    newList = []
    while indOne < len(list_one):
        elementListOne = list_one[indOne]
        indTwo = 0

        while indTwo < len(list_two):
            elementListTwo = list_two[indTwo]
            if elementListOne == elementListTwo:
                newList.append(elementListOne)
                break #sugestao do chatgpt para otimizar
            indTwo += 1
        indOne += 1
    return newList

print(concat_lists(['a', 'b', 'c'], ['a', 'a']))