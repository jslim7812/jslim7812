# 소스 실행시 오류가 있습니다. 아래의 수정사항을 적용하시오.
# 1. 파일 열 때 utf==8 인코딩을 설정하시오.
# 2. 파일은 상대경로로 설정하시오.

# 소스에서 파일의 상대경로를 사용하고자 한다면 "Open in Terminal" 에서 직접 실행하여야 한다.
# 터미널에서 python .\py31_03_filewrite.py 입력



import os.path

outfile = open("phones.txt", "a")

if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 이미 존재합니다.")

else:
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5680")

outfile.close()
