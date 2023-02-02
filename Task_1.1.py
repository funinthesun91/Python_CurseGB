number = int(input("Введите трехзначное число: "))
a = number % 10
b = (number // 10) % 10
c = number // 10 // 10
print(f"Сумма чисел равна: {a+b+c}")
