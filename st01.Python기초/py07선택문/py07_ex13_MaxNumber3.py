a = input("첫번째 수를 입력하세요. :")
b = input("두번째 수를 입력하세요. :")
c = input("세번째 수를 입력하세요. :")

if a > b:
    if a > c:
        print("입력 받은 수중 가장 큰 수는", a, "입니다.")
    else:
        print("입력 받은 수중 가장 큰 수는", c, "입니다.")
else:
    if b > c:
        print("입력 받은 수중 가장 큰 수는", b, "입니다.")
    else:
        print("입력 받은 수중 가장 큰 수는", c, "입니다.")
