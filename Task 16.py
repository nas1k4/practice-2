a = int(input())
b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
e = (a // 1000) % 10
if (a <= 9999) and (not(1900 < a < 2050)) and (b != c) and (c != d) and (b != d) and (e != d) and (b != e) and (e != c):
    print("OK")
else:
    print("ERROR")