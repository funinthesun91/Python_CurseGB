def closest_number(lst, X):
    closest = lst[0]
    min_diff = abs(lst[0] - X)
    for num in lst:
        if abs(num - X) < min_diff:
            closest = num
            min_diff = abs(num - X)
    return closest


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
X = int(input("Введите числоr: "))
result = closest_number(lst, X)
print("Самое близкое по величине число:", result)
