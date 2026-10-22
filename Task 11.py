import math
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
if (x - xc)**2 + (y - yc)**2 < r**2:
    print("точка вутри окружности")
elif (x - xc)**2 + (y - yc)**2 > r**2:
    print("точка вне окружности")
else:
    print('точка лежит на окружности')