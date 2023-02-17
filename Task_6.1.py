a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность (шаг) прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

an = a1 + (n-1) * d

print(a1)

for i in range(1, n):
    element = a1 + i * d
    print(element)