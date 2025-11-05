size = get_world_size()
counter = 0
def zbieranie(x):
	if x == size*size:
		harvest()
	else:
		return

while True:
	for x in range(size):
		for y in range(size):
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Pumpkin)
				if can_harvest():
					counter += 1
			else:
				plant(Entities.Pumpkin)
				if can_harvest():
					counter += 1
			move(East)
		move(North)
	zbieranie(counter)
	counter = 0