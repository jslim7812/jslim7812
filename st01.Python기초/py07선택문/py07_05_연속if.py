# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고
# 90점 이상이면 A,    90이상 100이하
# 80점 이상이면 B,    80이상 90미만
# 70점 이상이면 C,    70이상 80미만
# 60점 이상이면 D,    60이상 70미만
# 나머지는 F             60미만


a = input("점수:")
a = int(a)

if 90 <= a <= 100:
    print("Grade: A")
elif 80 <= a < 90:
    print("Grade: B")
elif 70 <= a < 80:
    print("Grade: C")
elif 60 <= a < 70:
    print("Grade: D")
else:
    print("Grade: F")
