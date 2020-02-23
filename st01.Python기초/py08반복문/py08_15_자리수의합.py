i=input("입력:")
i=int(i)

n1=i//1000
i=i-n1*1000
n2=i//100
i=i-n2*100
n3=i//10
i=i-n3*10
n4=i
sum=n1+n2+n3+n4
str="자리수의 합은 %s+%s+%s+%s=%s입니다." %(n1,n2,n3,n4, sum)
print(str)

===============================================
#문자열 정수의 길이를 구한다.
# 0부터 길이-1까지 1씩 증가시키면서
# 문자 한 개를 껀애 정수로 변환
# sum 을 구한다.

a=input("정수입력")
b=len(a)
sum=0
for i in range(0,b+1,1):
    x=int(a[i])
    sum=sum+x
    

a=str(a)
a1=int(a[0])
a2=int(a[1])
a3=int(a[2])
a4=int(a[3])
print(a1+a2+a3+a4)
