# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 



# 거스름돈(500원 동전 개수)을 계산한다. 

# 거스름돈(100원 동전 개수)을 계산한다. 

# 거스름돈(10원 동전 개수)을 계산한다. 

# 거스름돈(1원 동전 개수)을 계산한다. 

# 출력

price=input("물건값을 입력하시오:")
print()

w1000=input("1000원 지폐개수:")
w500=input("500원 동전개수:")
w100=input("100원 동전개수:")
w10=input("10원 동전개수:")
w1=input("1원 동전개수:")

price=int(price)
w1000=int(w1000)
w500=int(w500)
w100=int(w100)
w10=int(w10)
w1=int(w1)

a=(w1000*1000)+(w500*500)+(w100*100)+(w10*10)+(w1*1)
b=a-price #거스름돈
c=b//500 #500원 개수
d=b%500 #500원 뺀 나머지 잔돈
e=d//100 #100원 개수
f=d%100 #100원 뺀 나머지 잔돈
g=f//10 #10원 개수
h=f%10 #10원 뺀 나머지 잔돈

print()
print ("낸    돈:", a,"원")
print ("가    격:", price,"원")
print ("거스름돈:", b,"원")
print()
print ("500원=", c,"개")
print ("100원=", e,"개" )
print (" 10원=", g,"개" )
print ("  1원=", h,"개")






