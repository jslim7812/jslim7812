# 교재 207~221 페이지
# import 방식
# 모듈 import : import 모듈이름
# 함수 import :  from 모듈이름 import 모듈함수
#  as import

import fibo # 같은 폴더에 fibo.py가 있는 경우

def main():
    val=fibo.fib2(5000) # 모듈명(fibo).함수명(fib2)
    print(val)

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()


