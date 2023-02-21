x = int(input())
r = int()
e = int()
n = int()
# разбиваем число, которое вводится на сотни, десятки и единицы
if x // 100 > 0:
    r = x // 100
if x % 100 // 10 > 0:
    e = x % 100 // 10
if 0 < x % 100 % 10 < 10:
    n = x % 100 % 10
# римские обозначения
one = 'I'
five = 'V'
ten = 'X'
fifty = 'L'
hundred = 'C'

hundreds = 'C'

# из арабской сс в римскую (единицы)
unit = str()
if 5 <= n < 9:
    unit = (five + (n - 5) * one)
elif n == 9:
    unit = one + ten
elif n == 1:
    unit = one
elif 1 < n < 5:
    unit = (5 - n) * one + five
# из арабской сс в римскую (десятки)
dozen = str()
if 5 <= e < 9:
    dozen = (fifty + (e - 5) * ten)
elif e == 9:
    dozen = ten + hundred
elif e == 1:
    dozen = ten
elif 1 < e < 5:
    dozen = (5 - e) * ten + fifty
# если число трехзначное
if r:
    print(hundreds + dozen + unit)
else: #если двухзначное
    print(dozen + unit)
