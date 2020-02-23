# 오류의 종류에 따라서 서로 다른 예외 처리가 가능하다.
n1 = input("숫자1 입력:")
n2 = input("숫자2 입력:")

try:
    n1 = int(n1)
    n2 = int(n2)

    res = n1/n2

except ValueError as ex:
    print("ValueError", ex) #로그파일에 저장하는 방식으로 수정필요
except ZeroDivisionError as ex:
    print("ZeroDivisionError", ex)

