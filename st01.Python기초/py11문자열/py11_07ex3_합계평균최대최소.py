a = "74 874 9883 73 9 73646 774"
b = a.split()
c = []
for n in b:
    n = int(n)
    c.append(n)

print(c)
print(sorted(c))
avg = sum(c)/len(c)

print("합계:", sum(c))
print("평균:", avg)
print("최대값:", max(c))
print("최소값:", min(c))


qqq = "12 34 56 78"
www = qqq.split()
eee = []
for i in www:
    i = int(i)
    eee.append(i)

print(qqq)
print(www)
print(eee)
print("합계:" ,sum(eee))
print("평균:", sum(eee)/len(eee))
print("최대값:", max(eee))
print("최소값:", min(eee))
