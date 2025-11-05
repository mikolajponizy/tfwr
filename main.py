def drzewo(x,y):
	if x % 2 == 0:
		if y % 2 != 0:
			return True
		else:
			return False
	else:
		return False


size = get_world_size()

while True:
	for x in range(size):
		for y in range(size):
			if drzewo(x,y):
				plant(Entities.Tree)
			move(East)
		move(North)
		