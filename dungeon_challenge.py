def findx(x, move_x, hp):
	resulting_x = x + move_x

	if resulting_x < 0 or resulting_x > 9:
		hp -= 5
	else:
		x = resulting_x

	return x, hp


def findy(y, move_y, hp):
	resulting_y = y + move_y

	if resulting_y < 0 or resulting_y > 9:
		hp -= 5
	else:
		y = resulting_y

	return y, hp


def move(player, direction):
	x, y, hp = player
	move_x, move_y = direction
	x, hp = findx(x, move_x, hp)
	y, hp = findy(y, move_y, hp)
	return x, y, hp


# EXAMPLES:
print(move((1, 1, 10), (-1, 0)))  # (0, 1, 10)
print(move((0, 1, 10), (-1, 0)))  # => (0, 1, 5)
print(move((0, 9, 5), (0, 1)))  # => (0, 9, 0)
