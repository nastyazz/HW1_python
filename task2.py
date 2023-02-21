x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 > 0 and y1 > 0) and (x2 > 0 and y2 > 0): #про 1 четверть
    print("YES")
elif (x1 < 0 and y1 > 0) and (x2 < 0 and y2 > 0): #про 2 четверть
    print("YES")
elif (x1 < 0 and y1 < 0) and (x2 < 0 and y2 < 0): #про 3 четверть
    print("YES")
elif (x1 > 0 and y1 < 0) and (x2 > 0 and y2 < 0): #про 4 четверть
    print("YES")
else:      #если ничего не подходит
    print("NO")
