n = int(input())
if n % 10 == 1 and n != 11:
#если число n делится с остатком на 10 и равянется одному или n не равняется 11
    print(n, 'korova')
elif 2 <= n % 10 <= 4 and n // 10 != 1:
# иначе если n делится на 10 с остатком и это больше или равно 2 и меньше или равно 4 и n делится на 10 и не равно 1
    print(n, 'korovy')
else:
    print(n, 'korov')