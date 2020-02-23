i = 0
sum = 0
while i <= 100:
    i = i+1
    if i % 3 == 0:
        sum = sum+i
str="1부터 100사이의 모든 3의 배수의 합은 %s입니다." %(sum)
print(str)
