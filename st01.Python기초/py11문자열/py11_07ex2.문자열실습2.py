# -*- coding: utf-8 -*-


# 도전 2. 형변환. 문자열을 정수로 바꾸기.
# 문자열 "3"을 정수 3으로 바꾸시오. 구글 검색
# temp2 = "3"

# 도전 3. 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.
temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.strip().split(" ")
print(type(array1), array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

print(array1[0], type(array1[0]))
print(array1[1], type(array1[2]))
print(array1[2], type(array1[2]))

for i in range(0, len(array1), 1):
    array1[i]=int(array1[i])
print (type(array1), array1)


array2 = []
for n in array1:
    n = int(n)
    array2.append(n)

print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]
print(sorted(array2))
print(max(array2))

if __name__=="__name__":
    main()