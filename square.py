def squared(value):
	output = None
	try:
		output = int(value)
	except ValueError:
		return value * len(value)
	else:
		return output * output


print(squared(2))
print(squared('2'))
print(squared('tim'))
