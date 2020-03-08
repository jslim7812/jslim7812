str ="""This was a great help. I applied this method to similiar problem and rather than cantact a SELECT statement. 
I created an event scheduled every couple hours to rebuild a view that pivots n amount of rows from one table into n columns on the others. 
It is a big help because before I was rebuilding the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not be an issue as the pivoted rows->columns represent types of training employees at a franchise have so the view will not ever break a few thousand rows."""

# 1. 파일 읽고 문자열에 텍스트 저장.
# 2. 줄바꿈 (\n)을 제거한다.  replace("\n", " ")
str = str.replace(".", "")
str = str.replace(",", "")
str = str.replace("\n", "")
str = str.replace("->", " ")

# 3. 딕셔너리 table을 만든다.
table ={}
# 4. 문자열을 split() 해서 array 리스트로 만든다.
array=str.split(" ")
# 5. 반복문을 사용하여 array리스트를 루푸 돌면서
#   1) 리스트 요소에서 첫글자를 추출한다.
#       선택 연산자[] 사용
#       key = array[i][0] 또는 key = i[0]
#   2) 대문자와 소문자를 구분하지 않도록 대문자로 치환한다.
#       key = key.upper()
#   3) 딕셔너리 table에서 키값중에 key가 있는지 확인한다.
#      ==> table에서 찾을 때는 get() 메서드나 in 연산자 사용
#   4) 있으면 table[key] = table[key] + "-"
#       없으면 table[key] = "-"
# 6. 찾기가 끝나면 table을 key, value 형태로 출력한다.
for i in range(0,len(array),1):
    key=array[i][0]
    key=key.upper()
    tmp=table.get(key)
    if tmp == None:
        table[key] = 1
    else:
        table[key]=table[key]+1
for item in table.items():
    # print("items>>>", item[0], item[1])
    print(item[0], item[0]*item[1])
