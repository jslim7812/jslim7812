
# 내장함수

# 사용자함수


def get_sum(x, y):
    sum = 0
    for i in range(x, y+1, 1):
        sum = sum+i
    str = "%s부터 %s까지의 합계:" % (x, y)
    print("함수출력", str, sum)

    return sum


sum1 = get_sum(1, 10)
sum2 = get_sum(1, 100)
sum3 = get_sum(100, sum2)
