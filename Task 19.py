
n, m = map(int, input().split())
k = int(input())
if k % m == 0 or k % n == 0:
    print("успешно")
else:
    print("неосуществимо")