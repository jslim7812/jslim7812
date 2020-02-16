w=input("가로:")
h=input("세로:")

try:
    w=float(w)
    h=float(h)
except ValueError:
    pass

area=w*h
perimeter=2*(w+h)

print("사각형의 넓이:", area)
print("사각형의 둘레:", perimeter)