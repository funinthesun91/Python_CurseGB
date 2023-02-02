ticket = int(input("Введите номер билета: "))
a = ticket // 1000
b = ticket % 1000

one = a // 100
two = (a // 10) % 10
three = a % 10
four = b // 100
five = (b // 10) % 10
six = b % 10
if (one+two+three) == (four+five+six):
    print('Билет счастливый')
else:
    print('Билет не счастливый')

# print(a, b, one, two, three, four, five, six)
