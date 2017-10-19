a = 5
b = 20
c = b, a
print(c[0])


def add(*nums):  # if we printed out *nums, we would see that it is a tuple.
	print('nums: ', *nums)
	total = 0
	for num in nums:
		total += num
		return total


def add2(base, *args):
	# *args has to follow the first parameter, UNLESS using **kwargs,
	# in that case the function would look like : def add2(*args, **kwargs):
	total = base
	for num in args:
		total += num
	return total


def multiply(*args):
	product = 1
	for arg in args:
		product *= arg
	return product


def packer(name=None, **kwargs):
	print(kwargs)


def unpacker(first_name=None, last_name=None):
	if first_name and last_name:
		print("Hi {} {}".format(first_name, last_name))
	else:
		print("Hi no name!")


course_minutes = {
	"Python Basics": 232,
	"Django Basics": 237,
	"Flask Basics": 189,
	"Java Basics": 133
}

for course, minutes in course_minutes.items():
	print("{} is {} minutes long".format(course, minutes))

list(enumerate("abc")) # --> [(0, 'a'), (1, 'b'), (2, 'c')]


# CHALLENGE 2
def reverse(words):
	reversed = ""
	for letter in list(words)[::-1]:
		reversed += letter
	return reversed


def stringcases(script):
	return script.upper(), script.lower(), script.title(), reverse(script)


print(stringcases('boner party'))  # --> ('BONER PARTY', 'boner party', 'Boner Party', 'ytrap renob')


# CHALLENGE 3
def combo(iter1, iter2):
	output = []
	if len(iter1) != len(iter2):
		return "arguments must have the same length!"

	count = 0
	while count < len(iter1):
		output.append((iter1[count], iter2[count]))
		count += 1
	return output