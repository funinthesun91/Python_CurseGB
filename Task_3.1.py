def count_x(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    if count == 0:
        return -1
    return count


lst = [1, 2, 3, 4, 5, 3, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
x = int(input("Введите номер: "))
print("Цифра", x, "появится в списке:", count_x(lst, x))
