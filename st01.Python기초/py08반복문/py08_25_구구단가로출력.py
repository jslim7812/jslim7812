# 2단부터 19단까지 구구단을 출력하는 프로그램

for x in range(2, 20, 1):
    for y in range(1, 10, 1):
        str="%2s*%s=%3s" %(x,y,x*y)
        if y==9:
            print (str, end=".")
        else:
            print (str, end=", ")
    print()
