set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

union1 = set1.union(set2)
union2 = set1 | set2
intersection1 = set1.intersection(set2)
intersection2 = set1 & set2
difference1 = set1.difference(set2)
difference2 = set1 - set2
unique1 = set1.symmetric_difference(set2)
unique2 = set1 ^ set2

COURSES = {
	"Python Basics": {"Python", "functions", "variables",
					  "booleans", "integers", "floats",
					  "arrays", "strings", "exceptions",
					  "conditions", "input", "loops"},
	"Java Basics": {"Java", "strings", "variables",
					"input", "exceptions", "integers",
					"booleans", "loops"},
	"PHP Basics": {"PHP", "variables", "conditions",
				   "integers", "floats", "strings",
				   "booleans", "HTML"},
	"Ruby Basics": {"Ruby", "strings", "floats",
					"integers", "conditions",
					"functions", "input"}
}


def covers(focus):
	output = []
	for topic in COURSES:
		if (len(focus & COURSES[topic])) > 0:
			output.append(topic)
	return output


print(covers({"Python"}))


def covers_all(single_set):
	standard = len(single_set)
	output = []

	for topic in COURSES:
		temp = single_set & COURSES[topic]
		if len(temp) == standard:
			output.append(topic)

	return output
