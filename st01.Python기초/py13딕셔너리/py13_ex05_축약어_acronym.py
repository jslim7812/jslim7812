table = {"B4": "Before",
         "TX": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have a Nice Day"}

# 번역할 문장을 입력하시오 : TX Mr. Park!
#  결과 : Thanks Mr. Park!

# 1. 문자열을 split() 해서 array 리스트로 만든다.
# 2. 반복문을 사용하여 array 리스트를 루프를 돌리면서 딕셔너리 table에서 찾는다.
#   ==> table에서 찾을 때는 get() 메서드나 in 연산자를 사용한다.
# 3. 찾았다면 바꾼다. replace()
# 4. 출력한다.  문자열 join() 메서드를 사용하는 것으로 작성한다.

#문장 = input("번역할 문장을 입력하시오:")
문장 = "TX Mr. Park!"
array = 문장.split("")
for i in array:
    value = table.get(i)
    if valeu = None:
        
    문장.replace(i, value)

