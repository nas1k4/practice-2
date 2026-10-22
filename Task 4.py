a,b = map(int, input("Введите счет (два числа через пробел): ").split(":"))
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)