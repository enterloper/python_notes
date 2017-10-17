def packer(**kwargs):
	print(kwargs)


def unpacker(first_name=None, last_name=None):
	if first_name and last_name:
		print('Hi {} {}'.format(first_name, last_name))
	else:
		print('Hello no name!')


def packer2(name=None, **kwargs):
	print(kwargs)


packer(name='Kenneth', num=42, spanish_inquisition=None)
packer2(name='Richard', num=666, spanish_inquisition=None)
unpacker(**{"last_name": "Boothe", "first_name": "Richard"})





foodies = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]


def string_factory(yelpers):
	output = []
	for yelper in yelpers:
		output.append("Hi, I'm {} and I love to eat {}!".format(yelper['name'], yelper['food']))
	return output


string_factory(foodies)