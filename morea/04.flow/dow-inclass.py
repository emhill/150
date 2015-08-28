# What time should I wake up?

DoW = input("Day of Week? ").lower().rstrip("day")

#print(DoW)
#SATURDAY Saturday
if DoW == "sun":
	print("Wake up at 10 am")
elif DoW == "sat" or DoW == "satur":
	print("Wake up at 9 am")
elif DoW == "mon" or DoW == "tues" or \
DoW == "wednes" or DoW == "wed" or DoW == "thurs" or \
DoW == "fri":
	print("Wake up at 7 am")
else:
	print("Invalid day")
	
#elif (DoW == "monday" or DoW == "mon"...):
#	print("Wake up at 7 am")
#else:
#	print("Invalid day")