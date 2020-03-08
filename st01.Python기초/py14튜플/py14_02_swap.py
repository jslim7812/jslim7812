# swap 이란? 변수의 값을 바꾸는 코딩 기법
# 1. 외팔이 기법 (모든 프로그래밍 언어에서 가능)
x = 2
y = 3
print(x, y)
tmp = x
x = y
y = tmp
print(x, y)

# 2. 튜플을 사용하는 방법 (파이썬에서만 가능)
x = 2
y = 3
print("x=", x, "y=", y)
(x,y) = (y,x)
print("x=", x, "y=", y)
