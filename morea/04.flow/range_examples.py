# Range examples
# Emily Hill

print("-------------- range(1, 15, 3) ------------")
for a in range(1,15,3):
    print(a)

print("-------------- range(5, -15, -5) ------------")
for b in range(5, -15, -5):
    print(b)
    
# Won't display anything
print("-------------- range(5, -15, 5) ------------")
for counter in range(5, -15, 5):
    print(counter)

# Won't display anything
print("-------------- range(-5, 15, -5) ------------")
for counter in range(-5, 15, -5):
    print(counter)

print("-------------- range(5.5, 15, 1.5) ------------")
# Note that range expects integer values
for counter in range(5.5, 15, 1):
    print(counter)
