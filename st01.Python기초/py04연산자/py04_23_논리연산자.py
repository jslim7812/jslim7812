x=3
y=4

r=((x==3) and (y==3)) # True and False
print("(x==3) and (y==3):", r)

r=((x==3) and (y!=3)) # True and False
print("(x==3) and (y!=3):", r)

r=((x==3) or (y==3)) # True or False
print("(x==3) or (y==3):", r)

r=((x==3) or (y==4)) # True or False
print("(x==3) or (y==4):", r)

r=((x!=3) or (y==4)) # False or True
print("(x!=3) or (y==4):", r)

r=((x!=3) or (y!=4)) # False or True
print("(x!=3) or (y!=4):", r)

print((x==y)and(x!=y))
print((x>y)or(x<y))
print((x>y)or(x<y))
print((x>=y)or(x<=y))
print((x==y)and(x!=y)or(x<y))
