def drzewo(x,y):
	if x % 2 == 0:
		if y % 2 != 0:
			return True
		else:
			return False
	else:
		return False
	
def marchew(x,y):
	if x % 2 == 0:
		if y % 2 != 0:
			return False
		else:
			return True
	else:
		return False
	
def podlewanie(x,y):
	if get_water() < 0.25:
		use_item(Items.Water)


size = get_world_size()

while True:
	for x in range(size):
		for y in range(size):
			if drzewo(x,y):
				if can_harvest():
					harvest()
				plant(Entities.Tree)
				podlewanie(x,y)
			elif marchew(x,y):
				if get_ground_type() != Grounds.Soil:
					if can_harvest():
						harvest()
					till()
					plant(Entities.Carrot)
					podlewanie(x,y)
				else:
					if can_harvest():
						harvest()
					plant(Entities.Carrot)
					podlewanie(x,y)
			else:
				if can_harvest():
					harvest()
				plant(Entities.Grass)
				podlewanie(x,y)
			move(East)
		move(North)
