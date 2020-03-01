a = []
for 정수 in range(0, 10, 1):
    b = int(input("입력:"))
    a.append(b)

print("Input:", a)
a.sort()
print("리스트 정렬 후:", a)
print("최대값:", max(a))
print("최소값:", min(a))