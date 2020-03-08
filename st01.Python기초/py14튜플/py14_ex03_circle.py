import math  # pi=3.14159...... 변수를 사용하기 위해서 import


def calCircle(r):
    면적 = math.pi*r*r
    둘레 = 2*math.pi*r
    return(면적, 둘레)


def main():
    str = input("원의 반지름을 입력하시오:")
    r = float(str)
    (x, y) = calCircle(r)

    tmp = "원의 넓이는 %10.4f, 둘레는 %10.4f이다." % (x, y)
    print(tmp)

# main 함수 호출
if __name__=="__main__":
    main()
    


