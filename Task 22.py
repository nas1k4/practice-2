import math
n, k, m = map(int, input().split())
# Считаем количество поездок с округлением вверх
a = math.ceil(n / k)
b = a * 2 * m
print(b)