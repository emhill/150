# What does the following code output?

x = 2
y = 3
z = 4

b = x==2
c = not b
d = (y<4) and (z<3)

print("d=",d)

d = (y<4) or (z<3)
print("d=",d)

d = not d
print("b:", b, "c:", c, "d:", d)
