i="I eat %d apples." % 3
print(i)
'I eat 3 apples.'

number = 10
day = "three"
j="I ate %d apples. so I was sick for %s days." % (number, day)
print(j)

# 'I ate 10 apples. so I was sick for three days.'


# 정렬과 공백 (***사용빈도 높음***)
k="%10s" % "hi"  # '        hi'
l="%-10sjane." % 'hi'  # 'hi        jane.'
print(k)
print(l)

# 소수점 표현
m="%0.4f" % 3.42134234  # '3.4213'
n="%10.4f" % 3.42134234  # '    3.4213'
print(m)
print(n)
