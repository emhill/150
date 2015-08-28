import operator

# Find the mean, median, and mode in a list of numbers:
#1) list(range(1,11)); append(1); append(1)
#2) entered one per line in a file
#3) Write functions to read from file & calculate each statistic

def range_input():
	numbers = list(range(1,11))
	numbers.append(1)
	numbers.append(1)
	return numbers

def file_input(filename):
	with open(filename) as f:
		result = [int(line) for line in f]
	return result

def input_list(filename):
	file = open(filename)
	numbers = []
	for line in file:
		numbers.append(int(line))
	return numbers

def mean(numbers):
	return sum(numbers) / len(numbers)

def median(numbers):
	count = len(numbers)
	#print(numbers, "Count: ", count, numbers[count // 2])
	if count % 2 == 0: # even
		median = numbers[count // 2 - 1] + numbers[count // 2]
		median /= 2
	else:	# odd
		median = numbers[count // 2]
	return median

def mode(numbers):
	freq = {}
	for n in numbers:
		if n in freq:
			freq[n]+=1
		else:
			freq[n] = 1
	#return sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[0][0]
	mode = 0
	mode_freq = 0
	for key in freq:
		if mode_freq < freq[key]:
			mode_freq = freq[key]
			mode = key
	return mode

numbers = file_input("numbers.txt")
numbers = input_list("numbers.txt")
#numbers = range_input()
numbers.sort()
#print(numbers)

print("Mean:", mean(numbers))
print("Medn:", median(numbers))
print("Mode:", mode(numbers))