
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오
# 한 행씩 읽어 들여 파일에 쓰는 프로그램을 작성한다.



from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()

a = open(readFile, "r")
b= open("output.txt", "w")
for s in a:
    b.write(s)
    print(s)

