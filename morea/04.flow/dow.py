# What time should I wake up?

DoW = input("Day of Week? ").lower()

#print(DoW)
#SATURDAY Saturday
if (DoW == "sunday" or DoW == "sun"):
	print("Wake up at 10 am")
elif (DoW == "saturday" or DoW == "sat"):
	print("Wake up at 9 am")
else: # Monday Tuesday... January, Burger, Fries
	print("Wake up at 7 am")
	
#elif (DoW == "monday" or DoW == "mon"...):
#	print("Wake up at 7 am")
#else:
#	print("Invalid day")