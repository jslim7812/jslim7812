def get_sum(x, y):
    sum = 0
    for i in range(x, y+1, 1):
        sum = sum+i
    str = "%s부터 %s까지의 합계:" % (x, y)
    print("함수출력", str, sum)

    return sum


# 함수 호출
a = 3
b = 7
get_sum(a, b)


#  변수의 종류
# 전역 변수 : a, b => 함수에서 접근이 가능하다.
# 지역 변수 : i, sum, x, y
# 매개 변수 : x, y
