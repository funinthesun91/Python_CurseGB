def common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    if common:
        return sorted(list(common))
    else:
        return "Общих чисел нет"


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(common_numbers(list1, list2))
