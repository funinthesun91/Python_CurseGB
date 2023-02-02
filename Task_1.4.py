n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
k = int(input("Введите третье число: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
