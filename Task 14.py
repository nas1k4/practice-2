n = int(input())
g = n // 493
k = n - g * 493
if k >= 29:
    s = k // 29
    c = k % 29
    print(f"{g} галлеонов\n{s} сиклей\n{c} кнатов")
else:
    c = k % 29
    print(f"{g} галлеонов\n{c} кнатов")