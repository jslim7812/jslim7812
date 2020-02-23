# while 문을 사용하여 합계를 구하시오
# 무한반복과 반복문(루프) 탈출을 결합한 예제
# 교재134페이지 참조
# 무한반복문은 조건식을 True로 하면 된다.
# 루프탈출은 break를 사용


sum = 0
count = 0
while True:  # 무한루프
    입력값 = input("성적을 입력하시오:")
    입력값 = int(입력값)
    # 입력값이 음수이면 반복문을 종료 break
    if 입력값 < 0:
        break
    count = count+1  # 입력횟수
    sum=sum+입력값
평균값=sum/count
str="성적의 평균은 %s입니다." %(평균값)
print(str)


    
