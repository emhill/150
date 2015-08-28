# A

print("A:")
for x in range(1,6):
	print(x)

print("\nA different way:")

for x in range(5):
	print(x+1)
	
# B

print("\nB:")

for x in range(2, 12, 3):
	print(x)
	
# C

print("\nC:")

for x in range(3):
	print("****")

print("\nC using two loops:")

for i in range(3):
	for j in range(4):
		print("*", end='')
	print()
	
