# 입력 파일 이름과 출력 파일 이름을 받는다.

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.


# a=open("sales.txt", "w")

# while True:
    # i=input("일일매출:")
    # a.write(i)
##############################
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()

a = open(readFile, "r")
b= open("summary.txt", "w")
sum=0
avg=0
for s in a:
    s=int(s)
    s=sum+s
    print(s)
