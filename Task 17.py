a, b = map(float, input().split("x"))
r = 6.5
k = r * (2 ** 0.5)
if a <= k and b <= k:
    print("да")
else:
    print("нет")