# 소스 실행시 오류가 있습니다. 아래의 수정사항을 적용하시오.
# 1. 파일 저장할 때 utf-8인코딩을 설정하시오.
# 2. 실행하면 줄바꿈이 안된다. 어떻게 처리할 것인가?
# 3. 파일이 없으면 쓰기 모드로 파일을 여는 코드를 추가하시오.


# phones.txt 파일에 아래의 2줄 쓰고 저장하시오. 
# 최무선  010-1111-2222")
# 정중부  010-2222-3333

outfile = open("phones.txt", "a")

outfile.write("최무선 010-1111-2222\n")
outfile.write("정중부 010-2222-3333\n")

outfile.close()

file = open("phones.txt", "r") #, encoding="utf-8")
for s in file:
    print(s)