


#import sys
#sys.setrecursionlimit(0x10000)

mapa = [
			[0,0,0,0,0,0,0],
			[1,0,0,1,1,1,1],
			[1,0,0,1,1,1,1],
			[0,0,0,0,0,0,0],
			[0,0,1,1,0,0,0],
			[0,0,1,1,0,0,0]
		]

def find_island(mapa):
	islands = 0
	len_y = len(mapa)
	len_x = len(mapa[0])
	for y in range(0, len_y):
		for x in range(0, len_x):
			if(mapa[y][x] == 1):
				islands+=1
			mark_island(mapa, x, y, len_x, len_y)
	print(islands)
	return islands

def mark_island(mapa, x, y, len_x, len_y):
	if(x < len_x and y < len_y and x>=0 and y>=0 and mapa[x][y] == 1):
		mapa[y][x] = 2
	else:
		return
	#print("x:{},y:{}".format(x,y))
	mark_island(mapa, x+1, y, len_x, len_y)
	mark_island(mapa, x-1, y, len_x, len_y)
	mark_island(mapa, x, y+1, len_x, len_y)
	mark_island(mapa, x, y-1, len_x, len_y)

find_island(mapa)


