# 리스트 선언

# 리스트에 값을 대입

# for문을 사용하여 리스트에 값을 대입

# 표준입력 리스트에 저장하기

# for문을 사용하여 리스트의 값 출력

# 리스트와  for 문

# 문자열과 for 문
a = []
i = 0
n = 1
print("종료하려면 음수를 입력하시오.")
while True:
    i = int(input("성적%d을(를) 입력하시오:" % n))
    a.append(i)
    n = n+1
    if i < 0:
        break
a.pop(-1)
print(a)
print("합계:", sum(a))
print("평균:", sum(a)/len(a))
