# 용어설명
#  - 모듈
#  - 패키지
#  - 라이브러리
#  - 프레임워크

# 모듈의 종류
#  - 사용자모듈 : 내가 만든 모듈
#        - 함수나 변수가 들어 있는 파일 1개
#  - 패키지란?
#        - 사용자 모듈을 묶어 놓은 것

# 피보나치 수열 모듈

def fib(n): # 피보나치 수열을 화면에 출력한다.
    a, b = 0, 1
    while b<n:
        print(b, end=" ")
        a,b=b, a+b
    print()

def fib2(n): # 피보나치 수열을 리스트로 반환
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

