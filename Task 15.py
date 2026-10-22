n, k, m = map(int, input().split())
a1 = abs(k - m)
a2 = n - a1
if a1 < a2:
    print(a1 - 1)
else:
    print(a2 - 1)