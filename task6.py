a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c
if d<0: #если дискриминат меньше нуля ничего не выводится
    print("")
elif d == 0: #если дискриминант равен нулю, высчитывается вон эта штука
    print(-b//2*a)
elif d>0: #если дискриминант больше нуля, рассматриваем 2 варианта
    print(-b + d//2*a, -b - d//2*a)