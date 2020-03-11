# exercise
some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'c', 'e', 'd']

duplicates = list(
    set([char for char in some_list if some_list.count(char) > 1]))

print(duplicates)
