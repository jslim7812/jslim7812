
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.

sum1 = 0
for x in range(1, 11, 1):
    sum1 = sum1+x
print("1부터 10까지의 합계:", sum1)

sum2 = 0
for x in range(1, 101, 1):
    sum2 = sum2+x
print("1부터 100까지의 합계:", sum2)

sum3 = 0
for x in range(100, sum2+1, 1):
    sum3 = sum3+x
    str="%s부터 %s까지의 합계:"%(100, sum2)
print(str, sum3)



# 반복 코드는 함수를 만들어 사용한다.

def get_sum(x,y):
    sum3=0
    for i in range(x,y+1,1):
        sum3=sum3+1
    str"%s부터 %s까지의 합계:"%(x, y)
    print(str, sum3)

# 함수 호출== 함수 사용
get_sum(1,10)
get_sum(1,100)
get_sum(,)
