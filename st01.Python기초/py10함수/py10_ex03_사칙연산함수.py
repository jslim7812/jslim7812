def Add(x, y):
    result = x+y
    return result  # 결과 반환


def Minus(x, y):
    result = x-y
    return result  # 결과 반환


def Mul(x, y):
    result = x*y
    return result  # 결과 반환


def Div(x, y):
    result = x/y
    return result  # 결과 반환


# 입력 받기

a = input("Fisrt Num:")
b = input("Second Num:")

# 문자열 정수 변환
a = int(a)
b = int(b)

# Add 함수 호출
value = Add(a, b)
print("Add:", value)  # Add() 결과 출력

# Minus 함수 호출
value = Minus(a, b)
print("Minus:", value)  # Minus() 결과 출력

# Mul 함수 호출
value = Mul(a, b)
print("Mul:", value)  # Mul() 결과 출력

# Div 함수 호출
value = Div(a, b)
print("Div:", value)  # Div() 결과 출력
