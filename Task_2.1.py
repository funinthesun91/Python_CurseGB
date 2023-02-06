n = int(input("Введите количество монет: "))
a = 0
for i in range(n):
    b = int(input())
    if b == 1:
        a += 1
print(k if a < n/2 else n-a)
