# py02_09ex1_Salary

# 변수 선언 : salary , deposit 정수 변수 선언

# 정수를 입력받고 salary 변수 에 저장하시오.

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.


value1=input("첫번째 과목점수를 입력하세요")
value2=input("두번째 과목점수를 입력하세요")

value1=int(value1)
value2=int(value2)
sum=value1+value2
average = sum/2

print("------------------")
print ("average:", average)
if average>=95 :
    print ("very good")
else :
    print("just good")
print("------------------")
