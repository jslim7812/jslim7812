
# 리스트의 선언


# 리스트에 값을 대입


# 반복문을 사용하여 리스트에 값을 대입
#  0  -->  0
#  1  -->  10
#  2  -->  20
#  3  -->  30
#  4  -->  40
#  5  -->  5

# 반복문을 사용하여 리스트의 값 출력


a = []
for i in range(0, 3):
    i = int(input("입력%s:"%(i+1)))
    a.append(i)
print(a)

