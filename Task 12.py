a = int(input())
if a < 100:
    b = a % 10
    if 5 <= a <= 20:
        print(f"{a} попугаев")
    elif a >= 21 and b == 1 or a == 1:
        print(f'{a} попугай')
    elif 1 < a <= 4 or a >= 22 and 1 < b <= 6:
        print(f"{a} попугая")
    else:
        print(f"{a} попугаев")