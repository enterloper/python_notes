# have a HELP command
# have a SHOW command

# make a list to hold onto your items.
shopping_list = []


def show_help():
	# print out instructions on how to use the app
	print("What should we pick up at the store?")
	print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to remove an item from your list.
""")

# print out the list
def show_list():
	print("Here's your list:")
	for item in shopping_list:
		print(item)

def add_to_list(new_item):
	# add new items to our list
	shopping_list.append(new_item)
	print("Added {}. List now has {} items. ".format(new_item, len(shopping_list)))

def remove_from_list():
	item_to_remove = input('Which item would you like to remove? ')
	not_removed = True
	for item in shopping_list:
		if item == item_to_remove:
			shopping_list.remove(item)
			print("Removing {} from list, list now has {} items".format(item, len(shopping_list)))
			not_removed = False
			break
		else:
			continue
	if not_removed:
		print("The item {} was not found in your list.".format(item_to_remove))


show_help()

while True:
	# ask for new items
	new_item = input("> ")
	# be able to quit the app
	if new_item == "DONE":
		show_list()
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()
		continue
	elif new_item == "REMOVE":
		remove_from_list()
		continue
	add_to_list(new_item)

